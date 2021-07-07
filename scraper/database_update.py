import keywords
import scraper
from elasticsearch import Elasticsearch
import time
from os import path

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
                es.update(index="verdicts", id=line[:-1], body=updated)


def update_missing_keywords():
    """
    Updates missing keywords in the keyword-field for the index 'verdicts'
    by using the documentnumbers in no_keywords.txt
    """
    # Ziehe Dokumentennummern ohne Keywords
    missing_keywords_list = []
    keyword_dict = {}
    with open("no_keywords.txt", "r", encoding='UTF-8') as file:
        for docnr in file:
            missing_keywords_list.append(docnr[:-1])
    # Resette die Liste
    f = open("no_keywords.txt", "w")
    f.close()

    # Lade bereits vorhandene Keywords
    with open("keywords.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            docnr, keyword_list = line.split("\t")
            keyword_dict[docnr] = list(keyword_list[1:-2].replace("\'", "").split(', '))

    n = len(missing_keywords_list)
    with open("keywords.txt", "a", encoding='UTF-8') as file:
        for i, docnr in enumerate(missing_keywords_list):
            json_object = es.get(index='verdicts', id=docnr)['_source']

            # Prüfe ob Keywords bereits vorhanden
            if docnr in keyword_dict:
                json_object['keywords'] = keyword_dict[docnr]
            else:
                # Generiere neue Keywords
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
            try:
                # Schreibe Keywords in ES
                es.update(index="verdicts", id=docnr, body=updated)
            except:
                print("Writing keywords for " + docnr + " in ES failed.")
                f = open("no_keywords.txt", "a")
                f.write(docnr + "\n")
                f.close()
        if i % 1000 == 0:
            print("\t", int(i / n * 100), "%")


def update_database(index="verdicts"):  # todo: index Variabel gestalten?
    """
    Updates an existing Elasticsearch-Database by scraping the newest verdicts from
    www.rechtsprechung-im-internet.de
    and adding them to the 'verdicts' index. and also adding new references to the 'verdict_nodes' index.
    """
    if es.indices.exists(index=index):
        tic = time.time()
        scraper.update_database()
        toc = time.time()
        print("Done! Time needed: {}".format(str(toc - tic)))
    else:
        print("Index to be updated does not exists!")


def initialize_database(index="verdicts"):  # todo: s.o.
    """
    Creates a new 'verdicts' and 'verdict_nodes' index in an existing Elasticsearch-Database by scraping all data from
    www.rechtsprechung-im-internet.de
    Existing indices with the same name will be overwritten!
    :param index:
    """
    tic = time.time()
    if es.indices.exists(index=index):
        es.indices.delete(index=index, ignore=[400, 404])
    if es.indices.exists(index="verdict_nodes"):
        es.indices.delete(index="verdict_nodes", ignore=[400, 404])
    f = open("links.txt", "w")
    f.close()
    f = open("present_documents.txt", "w")
    f.close()
    f = open("no_keywords.txt", "w")
    f.close()
    if not path.exists('keywords.txt'):
        f = open("keywords.txt", "w")
        f.close()

    scraper.update_database()
    print("Starting to generate keywords...")
    update_missing_keywords()
    print("Updating incoming references-count...")
    update_incoming_count()
    # todo: classification
    toc = time.time()
    print("Done! Time needed: {}".format(str(toc - tic)))


if __name__ == '__main__':
    initialize_database()
    # update_missing_keywords()
    # update_incoming_count()
