import keywords
import scraper
from elasticsearch import Elasticsearch
import time
from os import path
from shutil import copyfile
import requests

es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}], timeout=60)


def update_incoming_count():
    """
    Updates the incoming references count in the index 'verdicts' by copying the related field from the index
    'verdict_nodes'. This is necessary for generating an pageranking based on the reference-count.
    """
    with open("present_documents.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            json_object = es.get(index='verdicts', id=line[:-1])['_source']
            if es.exists(index='verdict_nodes', id=json_object['filenumber']):
                verdict_node = es.get(index='verdict_nodes', id=json_object['filenumber'])['_source']
                json_object['incoming_count'] = verdict_node['incoming_count']
                # Modify dict to fit ES Convention
                updated = {
                    'doc': json_object
                }
                # write in in ES
                es.update(index="verdicts", id=line[:-1], body=updated)


def update_missing_keywords():
    """
    Updates missing keywords in the keyword-field for the index 'verdicts' for all documentnumbers in no_keywords.txt.
    The Keywords will be read out of keywords.txt or new generated with IBM-Watson, if there are no existing keywords
    for a verdict in keywords.txt.
    """
    # Lade Dokumentennummern ohne Keywords in eine Liste
    missing_keywords_list = []
    keyword_dict = {}
    with open("no_keywords.txt", "r", encoding='UTF-8') as file:
        for docnr in file:
            missing_keywords_list.append(docnr[:-1])

    # Resette no_keywords.txt und erstelle vorher Backup-Kopie
    copyfile("no_keywords.txt.txt", "no_keywords_OLD.txt")
    f = open("no_keywords.txt", "w")
    f.close()

    # Lade bereits vorhandene Keywords in ein Dict
    with open("keywords.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            docnr, keyword_list = line.split("\t")
            keyword_dict[docnr] = list(keyword_list[1:-2].replace("\'", "").split(', '))

    n = len(missing_keywords_list)
    with open("keywords.txt", "a", encoding='UTF-8') as file:
        for i, docnr in enumerate(missing_keywords_list):
            # Lade entsprechenden Eintrag aus ES
            json_object = es.get(index='verdicts', id=docnr)['_source']

            # Prüfe ob Keywords bereits in keywords.txt vorhanden
            if docnr in keyword_dict:
                json_object['keywords'] = keyword_dict[docnr]
            else:
                # Generiere neue Keywords falls nicht in keywords.txt vorhanden
                json_object['keywords'] = keywords.prepare_and_generate_keywords(
                    json_object['documentnumber'],
                    json_object['title'],
                    json_object['tenor'],
                    json_object['offense'],
                    json_object['reasons'],
                    json_object['reasonfordecision'])
                # Schreibe neue Keywords in keywords.txt
                file.write(docnr + "\t" + str(json_object['keywords']) + "\n")

            # Modify dict to fit ES Convention
            updated = {
                'doc': json_object
            }

            # Schreibe Keywords in ES
            try:
                es.update(index="verdicts", id=docnr, body=updated)
            except:
                print("Writing keywords for " + docnr + " in ES failed.")
                f = open("no_keywords.txt", "a")
                f.write(docnr + "\n")
                f.close()

        # Prozentuale Fortschrittsanzeige auf Konsole bei großen Updates
        if i % 1000 == 0:
            print("\t", int(i / n * 100), "%")


def scrape_new_data(index="verdicts"):  # todo: index Variabel gestalten?
    """
    Updates an existing Elasticsearch-Database by scraping the newest verdicts from
    www.rechtsprechung-im-internet.de
    and adding them to the 'verdicts' index. and also adding new references to the 'verdict_nodes' index.
    """
    if es.indices.exists(index=index):
        tic = time.time()
        scraper.update_database()
        toc = time.time()
        print("Scraping done! Time needed: {}".format(str(toc - tic)))
    else:
        print("Index to be updated does not exists!")

def update_database(index="verdicts"):
    """
    Updates an existing Elasticsearch-Database by scraping the newest verdicts and adding references and keywords.
    :param index:
    """
    tic = time.time()
    print("Start scraping new Data ...")
    scrape_new_data(index)
    print("Starting to add missing keywords ...")
    update_missing_keywords()
    print("Updating incoming references-count ...")
    update_incoming_count()
    # todo: classification
    toc = time.time()
    print("Update finished! Time needed: {}".format(str(toc - tic)))


def initialize_database(index="verdicts"):  # todo: s.o.
    """
    Creates a new 'verdicts' and 'verdict_nodes' index in an existing Elasticsearch-Database by scraping all data from
    www.rechtsprechung-im-internet.de
    and also adding references and keywords.
    Existing indices with the same name will be overwritten!
    :param index:
    """
    # lösche existierende Indizes
    if es.indices.exists(index=index):
        k = input("Index, " + index + " already exists!\noverwrite? (1 = yes)")
        if k == 1:
            es.indices.delete(index=index, ignore=[400, 404])
        else:
            print("Database initialization terminated")
            quit()
    if es.indices.exists(index="verdict_nodes"):
        k = input("Index, verdict_nodes already exists!\noverwrite? (1 = yes)")
        if k == 1:
            es.indices.delete(index="verdict_nodes", ignore=[400, 404])
        else:
            print("Database initialization terminated")
            quit()
    # Initialisiere benötigte .txt Dateien
    f = open("links.txt", "w")
    f.close()
    f = open("present_documents.txt", "w")
    f.close()
    f = open("no_keywords.txt", "w")
    f.close()
    if not path.exists('keywords.txt'):
        f = open("keywords.txt", "w")
        # lade keywords.txt aus Git
        try:
            url_keywords = "https://raw.githubusercontent.com/8fuhst/BLS_Projekt/master/scraper/keywords.txt"
            r = requests.get(url_keywords)
            f.write(r.content)  # todo testen
        finally:
            f.close()

    # start the initialisation process
    tic = time.time()
    print("Start scraping the Data ...")
    scraper.update_database()
    print("Starting to generate keywords ...")
    update_missing_keywords()
    print("Updating incoming references-count ...")
    update_incoming_count()
    # todo: classification
    toc = time.time()
    print("Done! Time needed: {}".format(str(toc - tic)))


if __name__ == '__main__':
    initialize_database()
    # update_missing_keywords()
    # update_incoming_count()
