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
import time
import formatter
# import classification as classi
import keywords

es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}], timeout=60)
#es = Elasticsearch([{'host': 'localhost', 'port': 9200}], timeout=60)

# TODO: Call once per day
def update_xml_table_of_contents(): # todo uncomment this
    """
    Gets the updated xml table of contents file from the website and writes it to the rii-toc.xml file using pycurl.
    :return:
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

#update_xml_table_of_contents()

def get_xml_from_file(xml_link):
    """
    Unzips the file and converts its content to xml string
    :param xml_link: link for zip file
    """
    first_xml = urlopen(xml_link)
    # Unzip XML file
    zipfile = ZipFile(BytesIO(first_xml.read()))
    # Get XML contents
    xml_string = zipfile.read(zipfile.namelist()[len(zipfile.namelist())-1]).decode("utf_8")
    return eval_xml(xml_string)


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

            '''if tag == 'tenor':
                if len(result_dict['tenor']) > 0:
                    tenor_text = result_dict['tenor']
                    preprocessed_tenor_text = formatter.replace_abbreviations(tenor_text)
                    # TODO Model anfunken und tenor reinkloppen, Result mit in ES speichern
                else:
                    # result is always neutral if there is no tenor
                    json_text = json.loads(result_dict)
                    json_text.update({"result": "neutral"})''' #TODO Weiterbauen

    # extract keywords from the text using watson api:
    # result_dict['keywords'] = keywords.prepare_and_generate_keywords(
    #     result_dict['documentnumber'],
    #     result_dict['title'],
    #     result_dict['tenor'],
    #     result_dict['offense'],
    #     result_dict['reasons'],
    #     result_dict['reasonfordecision'])

    result_dict['keywords'] = []
    result_dict['incoming_count'] = -1
    result_dict['successful'] = ""  # TODO Classifier aufrufen:
    # result_dict['successful'] = classi.classify(result_dict['tenor'])  # todo performance

    # build provisional reference-dict for ES that does not contain incoming references yet:
    provisional_references_dict = create_reference_dict(result_dict['filenumber'], outgoing_references_dict, outgoing_references_set, [], result_dict['documentnumber'])
    # ES fields: [ID][filenumber][list outgoing references][set outgoing references][set incoming references]
    # [sum of incoming references]

    #json_reference_dict = json.dumps(provisional_references_dict)
    #json_result_dict = json.dumps(result_dict)  # convert dictionary to json
    #return json_result_dict, json_reference_dict
    return result_dict, provisional_references_dict

# get_xml_from_file("http://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/JURE100055033.zip")


def extract_links_from_toc_xml():
    """
    Writes the links of zip files in links.txt
    """
    doc = ET.parse("./rii-toc.xml")  # Create ElementTree from rii-toc
    root = doc.getroot()             # Create root of ET
    # counter = 0  # todo remove this
    with open("links.txt", "w") as file:
        for item in root:
            # if counter > 499: # todo remove
            #     break # todo remove
            file.write(str(item.find('link').text) + "\n")  # Extract all Links from rii-toc to links.txt
            # counter += 1 # todo remove


def create_reference_dict(filenumber, outgoing_reference_dict ={}, outgoing_reference_set = set(), incoming_reference_set = [], documentnumber = ""):
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
        json_object, json_reference_object = get_xml_from_file(link)
        json_list.append(json_object)
        json_reference_list.append(json_reference_object)
        counter += 1
        if counter % 1000 == 0:
            print("\t", int(counter / n * 100), "%")
    return json_list, json_reference_list


def write_to_database(json_list, json_reference_list):
    # Save Verdicts in Elasticsearch
    print("writing verdicts...")
    counter = 0
    n = len(json_list)
    with open("present_documents.txt", "a", encoding='UTF-8') as f:
        with open("no_keywords.txt", "a", encoding='UTF-8') as g:
            for json_object in json_list:
                #es_json_object = json.dumps(json_object) # TODO Rename all things json
                # es.index(index='verdicts', body=json_object) #todo so hat es auf jeden fall funktioniert'
                es.index(index='verdicts', id=json_object['documentnumber'], body=json_object)
                f.write(json_object['documentnumber'] + "\n")
                g.write(json_object['documentnumber'] + "\n")
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
            json_reference_object['outgoing_reference_list']) # TODO extend() statt append()
            to_be_updated['outgoing_reference_set'].extend(json_reference_object['outgoing_reference_set'])
            to_be_updated['documentnumber'] = docnr  # update juris number
            # Modify dict to fit ES Convention
            updated = {
                'doc': to_be_updated
            }
            # Update ES Document with new References
            es.update(index="verdict_nodes", id=filenr, body=updated)

        counter += 1
        if counter % 1000 == 0:
            print("\t", int(counter / n * 100), "%")


def update_database():
    # with open("oldlinks.txt", "r", encoding='UTF-8') as file:
    #     # was ist der höchste idenfier
    #
    #     count = 0 # count = höchster identifier oder 0
    #     for line in file.readlines():
    #         json_object = get_xml_from_file(line)
    #         es.index(index='verdicts', doc_type='verdict', id=count, body=json_object)
    #         count = count + 1

    # Getting new links
    linklist = extract_new_links()

    print("Building JSON-Objects...")
    json_list, json_reference_list = build_json_objects(linklist)

    if len(linklist) == len(json_list):
        print("Starting to write to Database...")
        write_to_database(json_list, json_reference_list) # todo: Robust gegen Schreibfehler machen -> links.txt anpassen
        print(len(json_list), "new Verdicts added to ES")
    else:
        copyfile("oldlinks.txt", "links.txt")
        raise Exception("Refresh failed!")


def extract_new_links():
    print("Updating rii-toc.xml...")
    update_xml_table_of_contents()
    copyfile("links.txt", "oldlinks.txt")
    print("Extracting links...")
    extract_links_from_toc_xml()
    link_set = set()
    new_links = []
    # build difference list between old- and new-links
    with open("oldlinks.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            link_set.add(line)
    with open("links.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            if not line in link_set:
                new_links.append(line)
    return new_links


# extract_new_links()

#incoming_reference_set = ["filenr"]
#provisional_references_dict = json.dumps(create_reference_dict("reference", [], set(), incoming_reference_set))
#print(provisional_references_dict)

#print(get_xml_from_file("http://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/KVRE426901801.zip"))

#print(es.get(index='verdicts', doc_type='verdict', id=0))

# get_xml_files()
#extract_links_from_toc_xml()