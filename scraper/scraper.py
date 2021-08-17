import traceback

from bs4 import BeautifulSoup
import requests
import pycurl
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from xml.etree import ElementTree as ET
import certifi
import json
from elasticsearch import Elasticsearch
from shutil import copyfile
import references as ref
import formatter

es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}], timeout=60)

def update_xml_table_of_contents():
    """
    Gets the updated xml table of contents file from
    https://www.rechtsprechung-im-internet.de/
    and writes it to the rii-toc.xml file using pycurl.
    """
    # Create curl object:
    curl = pycurl.Curl()
    # Set certificate:
    curl.setopt(pycurl.CAINFO, certifi.where())
    # Set URL:
    curl.setopt(pycurl.URL, 'https://www.rechtsprechung-im-internet.de/rii-toc.xml')
    with open('./rii-toc.xml', 'wb') as toc_file:
        curl.setopt(curl.WRITEFUNCTION, toc_file.write)
        curl.perform()
    curl.close()


def get_xml_from_link(xml_link):
    """
    Unzips a file from an url and converts its content to xml string
    :param xml_link: link for zip file
    :return: the xml as utf-8 string
    :rtype: str xml_string
    """
    first_xml = urlopen(xml_link)
    # Unzip XML file
    zipfile = ZipFile(BytesIO(first_xml.read()))
    # Get XML contents
    xml_string = zipfile.read(zipfile.namelist()[len(zipfile.namelist())-1]).decode("utf_8")
    return xml_string


def eval_xml(xml_string):
    """
    Extracts Dokumentennummer, ECLI, Gerichtstyp, Gerichtsort, Spruchkoerper, Entscheidungs-Datum, Aktenzeichen,
    Dokumententyp, Norm and Vorinstanz from an XML File. Also creates a provisional reference dictionary of the
    references found inside the verdict
    TODO: Get the description texts (long version) too
    """
    result_dict = {}
    provisional_references_dict = {}
    # Parse XML string
    doc = ET.fromstring(xml_string)
    # List containing the relevant tags
    tags = ['doknr', 'ecli', 'gertyp', 'gerort', 'spruchkoerper', 'entsch-datum', 'aktenzeichen', 'doktyp', 'norm', 'vorinstanz', 'gruende', 'entscheidungsgruende', 'identifier', 'sonstlt', 'abwmeinung', 'tatbestand', 'tenor', 'sonstosatz', 'leitsatz', 'titelzeile', 'mitwirkung', 'region']
    tags_translation = {'doknr': 'documentnumber',
                        'ecli': 'ecli',
                        'gertyp': 'court',
                        'gerort': 'courtlocation',
                        'spruchkoerper': 'spruchkoerper',
                        'entsch-datum': 'date',
                        'aktenzeichen': 'filenumber',
                        'doktyp': 'documenttype',
                        'entscheidungsgruende': 'reasonfordecision',
                        'abwmeinung': 'abwmeinung',
                        'sonstosatz': 'miscsentence',
                        'norm': 'norms',
                        'vorinstanz': 'previouscourt',
                        'gruende': 'reasons',
                        'identifier': 'identifier',
                        'sonstlt': 'other',
                        'tatbestand': 'offense',
                        'tenor': 'tenor',
                        'leitsatz': 'keysentence',
                        'titelzeile': 'title',
                        'mitwirkung': 'mitwirkung',
                        'region': 'region'}

    # Load each tag into dictionary:

    outgoing_references_dict = {}  # Contains additional information about where the references are
    outgoing_references_set = set()  # Contains only the referenced filenumbers
    for tag in tags:
        tag_array = []  # Contains child-tags
        # Iterate through child tags of a tag:
        for child in doc.find(tag).iter():
            if child.text and child.text.rstrip() != "":
                if tag == 'entsch-datum':
                    tag_array.append(int(child.text))  # Append child date to array as int
                else:
                    tag_array.append(child.text.strip())  # Append child tag to array
        # If the array only contains one element, or the tag doesn't have child-tags,
        # only load that tag into the directory. Array is empty if there is no value inside the tag:
        if len(tag_array) == 1:
            if tag == 'vorinstanz':
                outgoing_references, outgoing_references_set = ref.find_reference(tag_array, outgoing_references_set)
                #outgoing_references_dict.append(outgoing_references)
                outgoing_references_dict[tag] = outgoing_references
            # Enter Data into the correct translated dict entry
            result_dict[tags_translation[tag]] = tag_array[0]
        else:
            # Specific tags require search for references
            # This path also enters any tags that are contained in arrays
            reference_tags = ['gruende', 'tenor', 'entscheidungsgruende', 'tatbestand', 'leitsatz', 'vorinstanz']
            if tag in reference_tags:
                outgoing_references, outgoing_references_set = ref.find_reference(tag_array, outgoing_references_set)
                # outgoing_references_dict.append(outgoing_references)
                outgoing_references_dict[tag] = outgoing_references #todo tags_translation?
            result_dict[tags_translation[tag]] = tag_array

    result_dict['keywords'] = []
    result_dict['incoming_count'] = -1
    result_dict['successful'] = ""

    # build provisional reference-dict for ES that does not contain incoming references yet:
    provisional_references_dict = create_reference_dict(result_dict['filenumber'], outgoing_references_dict, outgoing_references_set, [], result_dict['documentnumber'])
    # ES fields: [ID][filenumber][list outgoing references][set outgoing references][set incoming references]
    # [sum of incoming references]

    return result_dict, provisional_references_dict

def extract_links_from_toc_xml():
    """
    Writes the links of zip files in links.txt
    """
    doc = ET.parse("./rii-toc.xml")  # Create ElementTree from rii-toc
    root = doc.getroot()             # Create root of ET
    with open("links.txt", "w") as file:
        for item in root:
            file.write(str(item.find('link').text) + "\n")  # Extract all Links from rii-toc to links.txt

def create_reference_dict(filenumber, outgoing_reference_dict={}, outgoing_reference_set=set(), incoming_reference_set=[], documentnumber=""):
    """
    Creates a reference-dict for a given filenumber.
    :param filenumber: the filenumber
    :param outgoing_reference_dict: outgoing reference-dict (contains the positions of the references)
    :param outgoing_reference_set: outgoing reference-set
    :param incoming_reference_set: incoming reference-set
    :param documentnumber: the documentnumber
    :return: the reference-dict
    :rtype: dict{str: filenumber, dict: outgoing_reference_dict, list: outgoing_reference_set, list: incoming_reference_set, int: incoming_count, str: documentnumber}
    """
    provisional_references_dict = {
        'filenumber': filenumber,
        'outgoing_reference_list': outgoing_reference_dict,
        'outgoing_reference_set': list(outgoing_reference_set),
        'incoming_reference_set': list(incoming_reference_set),
        'incoming_count': len(incoming_reference_set),
        'documentnumber': documentnumber
    }
    return provisional_references_dict


def build_json_objects(linklist):
    """
    Reads the links in the oldlinks.txt File, unzips them and extracts metadata.
    """
    json_list = []
    json_reference_list = []
    counter = 0
    n = len(linklist)
    for link in linklist:
        json_object, json_reference_object = eval_xml(get_xml_from_link(link))
        json_list.append(json_object)
        json_reference_list.append(json_reference_object)

        # Prozentuale Fortschrittsanzeige auf Konsole bei großen Updates
        counter += 1
        if counter % 1000 == 0:
            print("\t", int(counter / n * 100), "%")
    return json_list, json_reference_list


def write_to_database(json_list, json_reference_list):
    # Save Verdicts in Elasticsearch
    print("writing verdicts ...")
    counter = 0
    n = len(json_list)
    with open("present_documents.txt", "a", encoding='UTF-8') as f:
        with open("no_keywords.txt", "a", encoding='UTF-8') as g:
            for json_object in json_list:
                es.index(index='verdicts', id=json_object['documentnumber'], body=json_object)
                f.write(json_object['documentnumber'] + "\n")
                g.write(json_object['documentnumber'] + "\n")
                # Prozentuale Fortschrittsanzeige auf Konsole bei großen Updates
                counter += 1
                if counter % 1000 == 0:
                    print("\t", int(counter / n * 100), "%")

    # Save or create Verdict Node that contains references
    print("writing references...")
    counter = 0
    n = len(json_reference_list)
    for json_reference_object in json_reference_list:
        filenr = json_reference_object['filenumber']
        docnr = json_reference_object['documentnumber']
        for reference in json_reference_object['outgoing_reference_set']:
            # Update Verdict Node with new incoming Reference
            if es.exists(index="verdict_nodes", id=reference):
                # Fetch old data from ES
                to_be_updated = es.get(index="verdict_nodes", id=reference)['_source']
                # Append newest incoming Reference
                to_be_updated['incoming_reference_set'].append(filenr)
                to_be_updated['incoming_count'] = to_be_updated['incoming_count'] + 1

                # Modify dict to fit ES Convention
                updated = {
                    'doc': to_be_updated
                }

                # Update ES Document with new References
                es.update(index="verdict_nodes", id=reference, body=updated)

            else:
                # Add new verdict node into ES if a non-existant Verdict is referenced
                incoming_reference_set = [filenr]
                # create incoming reference from the verdict this json_reference_object belongs to
                # create new verdict node with only the incoming reference
                provisional_references_dict = create_reference_dict(reference, {}, set(), incoming_reference_set)
                json_reference_dict = json.dumps(provisional_references_dict)
                # add the new verdict node to ES
                es.index(index='verdict_nodes', id=reference, body=json_reference_dict)

        # Update Verdict Node for the current verdict
        if not es.exists(index="verdict_nodes", id=filenr):
            # Add the verdict node
            es_json_reference_object = json.dumps(json_reference_object)
            es.index(index='verdict_nodes', id=filenr, body=es_json_reference_object)
        else:
            # Fetch old data from ES
            to_be_updated = es.get(index="verdict_nodes", id=filenr)['_source']
            # Add the outgoing references
            to_be_updated['outgoing_reference_list'].update(
            json_reference_object['outgoing_reference_list'])
            to_be_updated['outgoing_reference_set'].extend(json_reference_object['outgoing_reference_set'])
            to_be_updated['documentnumber'] = docnr  # update juris number
            # Modify dict to fit ES Convention
            updated = {
                'doc': to_be_updated
            }
            # Update ES Document with new References
            es.update(index="verdict_nodes", id=filenr, body=updated)

        # Prozentuale Fortschrittsanzeige auf Konsole bei großen Updates
        counter += 1
        if counter % 1000 == 0:
            print("\t", int(counter / n * 100), "%")


def update_database():
    """
    Builds the json objects and then updates the elasticsearch database
    """
    # Getting new links
    linklist = extract_new_links()

    print("Building JSON-Objects...")
    json_list, json_reference_list = build_json_objects(linklist)

    if len(linklist) == len(json_list):
        print("Starting to write to Database ...")
        write_to_database(json_list, json_reference_list)
        print(len(json_list), "new Verdicts added to ES")
    else:
        copyfile("oldlinks.txt", "links.txt")
        raise Exception("Refresh failed!")


def extract_new_links():
    """
    Gets the newest rii-toc.xml from https://www.rechtsprechung-im-internet.de/ and builds a list of the new links out
    of it with help of the previous link.txt.
    The link.txt and oldlinks.txt will be overwitten in this process!
    :return: A list containing the new links (list of verdicts, which are not already in ES)
    :rtype: list(str: link)
    """
    # preparations
    print("Updating rii-toc.xml ...")
    update_xml_table_of_contents()
    copyfile("links.txt", "oldlinks.txt")

    # Update link.txt
    print("Extracting links ...")
    extract_links_from_toc_xml()

    # build difference list between old- and new-links
    link_set = set()
    new_links = []
    with open("oldlinks.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            link_set.add(line)
    with open("links.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            if line not in link_set:
                new_links.append(line)
    return new_links

