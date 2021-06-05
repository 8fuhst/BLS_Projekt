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

es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}])

# TODO: Call once per day
def update_xml_table_of_contents():
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
    Unzips the file and converts its to string
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
    Extracts Dokumentennummer, ECLI, Gerichtstyp, Gerichtsort, Spruchkoerper, Entscheidungs-Datum, Aktenzeichen, Dokumententyp, Norm and
    Vorinstanz from an XML File.
    TODO: Writes the extracted information into the database.
    TODO: Get the description texts (long version) too
    """
    result_dict = {}
    references_dict = {}
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

    reference_list =[]
    for tag in tags:
        tag_array = []  # Contains child-tags
        # Iterate through child tags of a tag:
        for child in doc.find(tag).iter():
            if child.text and not child.text.startswith("\n"):
                if tag == 'entsch-datum':
                    tag_array.append(int(child.text)) # Append child date to array as int
                else:
                    tag_array.append(child.text)  # Append child tag to array        # If the array only contains one element, or the tag doesn't have child-tags,
        # only load that tag into the directory. Array is empty if there is no value inside the tag:
        if len(tag_array) == 1:
            if tag == 'vorinstanz':
                references = ref.find_reference(tag, tag_array)
                reference_list.append(references)
            result_dict[tags_translation[tag]] = tag_array[0]
        else:
            reference_tags = ['gruende', 'tenor', 'entscheidungsgruende', 'tatbestand', 'leitsatz', 'vorinstanz']
            if tag in reference_tags:
                references = ref.find_reference(tag, tag_array)
                reference_list.append(references)
            result_dict[tags_translation[tag]] = tag_array
    references_dict[result_dict['filenumber']] = reference_list
    # print(references_dict)
    # print(result_dict)

    json_reference_dict = json.dumps(references_dict)
    json_result_dict = json.dumps(result_dict)  # convert dictionary to json
    return json_result_dict
    # print(json_result_dict)

# get_xml_from_file("http://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/JURE100055033.zip")


def extract_links_from_toc_xml():
    """
    Writes the links of zip files in oldlinks.txt
    """
    doc = ET.parse("./rii-toc.xml")
    root = doc.getroot()

    with open("links.txt", "w") as file:
        for item in root:
            file.write(str(item.find('link').text) + "\n")

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
    for link in linklist:
        json_object = get_xml_from_file(link)  # todo Bilder betrachten
        json_list.append(json_object)
    if len(linklist) == len(json_list):
         for json_object in json_list:
            es.index(index='verdicts', doc_type='verdict', body=json_object)  #todo wegnehmen um in datanbank zu speichern
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

#print(es.get(index='verdicts', doc_type='verdict', id=0))

# get_xml_files()
#extract_links_from_toc_xml()