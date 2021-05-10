from bs4 import BeautifulSoup
import requests
import pycurl
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from xml.etree import ElementTree as ET
import certifi


def extract_links(urlstring): # TODO: Löschen?
    site = requests.get(urlstring).text
    soup = BeautifulSoup(site, "lxml")
    upper_limit = remove_point(soup.find('strong', id='numberhits').text)
    with open("./links.txt", "a") as file:

        for i in range(1, upper_limit):
            article_id = 'tlid' + str(i)
            hit = soup.find('a', id=article_id)['href']
            file.write("https://www.rechtsprechung-im-internet.de/" + hit + "\n")
            #result_site = s.get("https://www.rechtsprechung-im-internet.de/" + hit).text
            #if i % 25 == 0:
                #site =

                # TODO Seiten ziehen von den einzelnen Suchergebnissen, Overflowen


def remove_point(passstring): # TODO: Löschen?
    modstring = passstring.replace('.', '')
    modstring = modstring.rsplit()[0]
    return int(modstring)

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
    xml_string = zipfile.read(zipfile.namelist()[0]).decode("utf-8")
    eval_xml(xml_string)


def eval_xml(xml_string):
    """
    Extracts Dokumentennummer, ECLI, Gerichtstyp, Gerichtsort, Spruchkoerper, Entscheidungs-Datum, Aktenzeichen, Dokumententyp, Norm and
    Vorinstanz from an XML File.
    TODO: Writes the extracted information into the database.
    TODO: Get the description texts (long version) too
    """
    # Parse XML string
    doc = ET.fromstring(xml_string)
    # List containing the relevant tags
    tags = ['doknr', 'ecli', 'gertyp', 'gerort', 'spruchkoerper', 'entsch-datum', 'aktenzeichen', 'doktyp', 'norm', 'vorinstanz']

    for tag in tags:
        tag_value = doc.find(tag).text
        if tag_value:
            print(tag + ": " + tag_value) # TODO: Was wenn wir missing Values in der DB haben?


get_xml_from_file("http://www.rechtsprechung-im-internet.de/jportal/docs/bsjrs/JURE100055033.zip")


def extract_links_from_toc_xml():
    """
    Writes the links of zip files in links.txt
    """
    doc = ET.parse("./rii-toc.xml")
    root = doc.getroot()
    with open("./links.txt", "a") as file:
        for item in root:
            file.write(str(item.find('link').text) + "\n")


def get_xml_files():
    """
    Reads the links in the links.txt File, unzips them and extracts metadata.
    """
    with open("./links.txt", "r") as file:
        for line in file.readlines():
            get_xml_from_file(line)

# get_xml_files()
#extract_links_from_toc_xml()