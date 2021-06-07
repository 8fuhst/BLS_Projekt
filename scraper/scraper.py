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

es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}])

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
    TODO: Writes the extracted information into the database.
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

    outgoing_references_list = []  # Contains additional information about where the references are
    outgoing_references_set = set()  # Contains only the referenced filenumbers
    for tag in tags:
        tag_array = []  # Contains child-tags
        # Iterate through child tags of a tag:
        for child in doc.find(tag).iter():
            if child.text and not child.text.startswith("\n"):
                if tag == 'entsch-datum':
                    tag_array.append(int(child.text))  # Append child date to array as int
                else:
                    tag_array.append(child.text)  # Append child tag to array
        # If the array only contains one element, or the tag doesn't have child-tags,
        # only load that tag into the directory. Array is empty if there is no value inside the tag:
        if len(tag_array) == 1:
            if tag == 'vorinstanz':
                outgoing_references, outgoing_references_set = ref.find_reference(tag, tag_array, outgoing_references_set)
                outgoing_references_list.append(outgoing_references)
            # Enter Data into the correct translated dict entry
            result_dict[tags_translation[tag]] = tag_array[0]
        else:
            # Specific tags require search for references
            # This path also enters any tags that are contained in arrays
            reference_tags = ['gruende', 'tenor', 'entscheidungsgruende', 'tatbestand', 'leitsatz', 'vorinstanz']
            if tag in reference_tags:
                outgoing_references, outgoing_references_set = ref.find_reference(tag, tag_array, outgoing_references_set)
                outgoing_references_list.append(outgoing_references)
            result_dict[tags_translation[tag]] = tag_array

    # build provisional reference-dict for ES that does not contain incoming references yet:
    provisional_references_dict = create_reference_dict(result_dict['filenumber'], outgoing_references_list, outgoing_references_set)
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
    counter = 0  # todo remove this
    with open("links.txt", "w") as file:
        for item in root:
            if counter > 100: # todo remove
                break # todo remove
            file.write(str(item.find('link').text) + "\n")  # Extract all Links from rii-toc to links.txt
            counter += 1 # todo remove

def create_reference_dict(filenumber, outgoing_reference_list = [], outgoing_reference_set = set(), incoming_reference_set = set()):
    provisional_references_dict = {
        'filenumber': filenumber,
        'outgoing_reference_list': outgoing_reference_list,
        'outgoing_reference_set': list(outgoing_reference_set),
        'incoming_reference_set': list(incoming_reference_set),
        'incoming_count': len(incoming_reference_set)
    }
    return provisional_references_dict

def update_database(linklist):
    """
    Reads the links in the oldlinks.txt File, unzips them and extracts metadata.
    """
    # with open("oldlinks.txt", "r", encoding='UTF-8') as file:
    #     # was ist der höchste idenfier
    #
    #     count = 0 # count = höchster identifier oder 0
    #     for line in file.readlines():
    #         json_object = get_xml_from_file(line)
    #         es.index(index='verdicts', doc_type='verdict', id=count, body=json_object)
    #         count = count + 1
    json_list = []
    json_reference_list = []
    for link in linklist:
        json_object, json_reference_object = get_xml_from_file(link)
        json_list.append(json_object)
        json_reference_list.append(json_reference_object)
    if len(linklist) == len(json_list):
        # Save Verdict in Elasticsearch
        for json_object in json_list:
            #es_json_object = json.dumps(json_object) # TODO Rename all things json
            es.index(index='verdicts2', doc_type='verdict', body=json_object)
        # Save or create Verdict Node that contains references
        for json_reference_object in json_reference_list:
            filenr = json_reference_object['filenumber']
            for reference in json_reference_object['outgoing_reference_set']:
                # Update Verdict Node with new incoming Reference
                if es.exists(index="verdict_nodes2", doc_type="verdict_node", id=reference):
                    # Fetch old data from ES
                    to_be_updated = es.get(index="verdict_nodes2", doc_type="verdict_node", id=reference)
                    # Append newest incoming Reference
                    to_be_updated['incoming_reference_set'] = to_be_updated['incoming_reference_set'] \
                        .append(filenr)
                    to_be_updated['incoming_count'] = to_be_updated['incoming_count'] + 1
                    # Modify dict to fit ES Convention
                    updated = {
                        'doc': to_be_updated
                    }
                    # Update ES Document with new References
                    es.update(index="verdict_nodes2", doc_type="verdict_node", id=reference, body=updated)
                else:
                    # Add new verdict node into ES if a non-existant Verdict is referenced
                    incoming_reference_set = set()
                    # create incoming reference from the verdict this json_reference_object belongs to
                    incoming_reference_set.add(filenr)
                    # create new verdict node with only the incoming reference
                    provisional_references_dict = create_reference_dict(reference, incoming_reference_set= incoming_reference_set)
                    json_reference_dict = json.dumps(provisional_references_dict)
                    # add the new verdict node to ES
                    es.index(index='verdict_nodes2', doc_type='verdict_nodes', id=filenr,
                             body=json_reference_dict)

            # Update Verdict Node for the current verdict
            if not es.exists(index="verdict_nodes2", doc_type="verdict_node", id=filenr):
                # Add the verdict node
                es.index(index='verdict_nodes2', doc_type='verdict_nodes',  id=filenr, body=json_reference_object)
            else:
                # Fetch old data from ES
                to_be_updated = es.get(index="verdict_nodes2", doc_type="verdict_node", id=filenr)
                # Add the outgoing references
                to_be_updated['outgoing_reference_list'] = json_reference_object['outgoing_reference_list']
                to_be_updated['outgoing_reference_set'] = json_reference_object['outgoing_reference_set']
                # Modify dict to fit ES Convention
                updated = {
                    'doc': to_be_updated
                }
                # Update ES Document with new References
                es.update(index="verdict_nodes2", doc_type="verdict_node", id=filenr, body=updated)
    else:
        print("Aktualisierung fehlgeschlagen")
        copyfile("oldlinks.txt", "links.txt")



def extract_new_links():
    update_xml_table_of_contents()
    copyfile("links.txt", "oldlinks.txt")
    extract_links_from_toc_xml()
    link_set = set()
    new_links = []
    with open("oldlinks.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            link_set.add(line)
    with open("links.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            if not line in link_set:
                new_links.append(line)
    update_database(new_links)

extract_new_links()

#print(get_xml_from_file("https://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/KVRE443342101.zip"))

#print(es.get(index='verdicts', doc_type='verdict', id=0))

# get_xml_files()
#extract_links_from_toc_xml()