from bs4 import BeautifulSoup
import requests
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
from xml.etree import cElementTree as ET

# Get first site
s = requests.Session()
test = s.get("https://www.rechtsprechung-im-internet.de/jportal/portal/page/bsjrsprod.psml")
site = s.get("https://www.rechtsprechung-im-internet.de/jportal/portal/t/ub6/page/bsjrsprod.psml/js_peid/Suchportlet1/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&form=bsjrsFastSearch&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkdtnBWABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEFxs4g79d4qNUZz6lwjiedwAAABAQKo%2BUP4vdOQay%2BOY6RAyUqPnVWUN8uku3lt9bBnEhV1y6jiVzUf0xWvmuE7XNX%2F4n52u4pp%2F1yBW9ELAn7kWEAAU4Nj9K1P4mzfXZxpjHrqp1FLROc0%3D&sugportalport=8080&sughashcode=752441794982660026236356826285894282340001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&desc=all&sug_all=&query=*&standardsuche.x=0&standardsuche.y=0&rqfcb=2571607").text
soup = BeautifulSoup(site, "lxml")
# Extract Link to first article

def extract_links(urlstring):
    site = requests.get(urlstring).text
    soup = BeautifulSoup(site, "lxml")
    upper_limit = remove_point(soup.find('strong', id='numberhits').text)
    print(upper_limit)
    for i in range(1, upper_limit):
        first_hit = soup.find('a', id='tlid1')['href']
        first_site = s.get("https://www.rechtsprechung-im-internet.de/" + first_hit).text
        #if i % 25 == 0:
            # TODO Seiten ziehen von den einzelnen Suchergebnissen


def remove_point(passstring):
    modstring = passstring.replace('.','')
    modstring = modstring.rsplit()[0]
    return int(modstring)

def get_xml(urlstring):
    urltext = requests.get(urlstring)
    urlsoup = BeautifulSoup(urltext, "lxml")
    # Get XML Link from site
    xml_link = urlsoup.find('a', {"name": "XML"})['href']

    # Get XML from site
    first_xml = urlopen("https://www.rechtsprechung-im-internet.de/" + xml_link)
    # Unzip XML file
    zipfile = ZipFile(BytesIO(first_xml.read()))
    # Get XML contents
    xml_string = zipfile.read(zipfile.namelist()[0]).decode("utf-8")


def eval_xml(xml_string):
    # Parse XML string
    doc = ET.fromstring(xml_string)
    # List containing the relevant tags
    tags = ['doknr', 'ecli', 'gertyp', 'gerort', 'spruchkoerper', 'entsch-datum', 'aktenzeichen', 'doktyp', 'norm', 'vorinstanz']

    for tag in tags:
        tag_value = doc.find(tag).text
        if tag_value:
            print(tag + ": " + tag_value) # TODO: Was wenn wir missing Values in der DB haben?

#doknr = doc.find('doknr').text
#print(doknr)

extract_links("https://www.rechtsprechung-im-internet.de/jportal/portal/t/1b7i/page/bsjrsprod.psml/js_peid/Suchportlet2/media-type/html?formhaschangedvalue=yes&eventSubmit_doSearch=suchen&action=portlets.jw.MainAction&deletemask=no&wt_form=1&sugline=-1&sugstart=&sugcountrows=10&sugshownorelevanz=false&sugactive=true&sugportal=ETMsDgAAAXkeWiZXABRBRVMvQ0JDL1BLQ1M1UGFkZGluZwCAABAAEPuGCLz7URi7GQwvY7ab0ugAAABAq22HIaRog0kgy%2FxMRsyk65cRVLT4CBhoYaJ2yBFucxEi63r9MPaG%2BTCoPCxweB340S7YDVDQC6hS0IZBgZVD5QAUX6fdTsVUZWzIwFXE0Z0iN%2B9xeEs%3D&sugportalport=8080&sughashcode=752441794982660026236356826285894282340001&sugwebhashcode=&sugcmspath=%2Fjportal%2Fcms%2F&form=jurisExpertSearch&desc=text&sug_text=&query=&desc=norm&sug_norm=&query=&desc=date&query=date&dateFrom=&dateTo=&desc=court_author&query=BVerfG&desc=filenumber&sug_filenumber=&query=&standardsuche=suchen")