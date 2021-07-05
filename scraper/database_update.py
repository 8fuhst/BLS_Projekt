import keywords
import scraper
from elasticsearch import Elasticsearch


es = Elasticsearch([{'host': 'basecamp-bigdata', 'port': 9200}], timeout=60)

def update_incoming_count():
    """
    Updates the incoming references count in the index 'verdicts' by copying the related field from the index
     'verdict_nodes'. This is necessary for generating an pageranking based on the reference-count.
    """
    with open("present_documents.txt", "r", encoding='UTF-8') as file:
        for line in file.readlines():
            json_object = es.get(index='verdict', id=line)
            if es.exists(index='verdict_nodes', id=json_object['filenumber']):
                verdict_node = es.get(index='verdict_nodes', id=json_object['filenumber'])
                json_object['incoming_count'] = verdict_node['incoming_count']
                # Modify dict to fit ES Convention
                updated = {
                    'doc': json_object
                }
                es.update(index="verdict", id=line, body=updated)

def update_missing_keywords():
    """
    Updates missing keywords in the keyword-field for the index 'verdicts'
    by using the documentnumbers in no_keywords.txt
    """
    missing_keywords_list = []
    with open("no_keywords.txt", "r", encoding='UTF-8') as file:
        for docnr in file:
            missing_keywords_list.append(docnr)
    f = open("no_keywords.txt", "w")
    f.close()
    for docnr in missing_keywords_list:
        json_object = es.get(index='verdict', id=docnr)
        json_object['keywords'] = keywords.prepare_and_generate_keywords(
        json_object['documentnumber'],
        json_object['title'],
        json_object['tenor'],
        json_object['offense'],
        json_object['reasons'],
        json_object['reasonfordecision'])

        # Modify dict to fit ES Convention
        updated = {
            'doc': json_object
        }
        es.update(index="verdict", id=docnr, body=updated)


def update_database():
    """
    Updates an existing Elasticsearch-Database by scraping the newest verdicts from
    www.rechtsprechung-im-internet.de
    and adding them to the 'verdicts' index. and also adding new references to the 'verdict_nodes' index.
    """
    scraper.extract_new_links()

def create_database(index = "verdicts"): # todo: index Variabel gestalten?
    """
    Creates a new 'verdicts' and 'verdict_nodes' index in an existing Elasticsearch-Database by scraping all data from
    www.rechtsprechung-im-internet.de
    Existing indexes with the same name will be overwritten!
    :param index:
    """
    es.indices.delete(index=index, ignore=[400, 404])
    es.indices.delete(index=index + "_nodes", ignore=[400, 404])
    f = open("links.txt", "w")
    f.close()
    f = open("present_documents.txt", "w")
    f.close()
    f = open("no_keywords.txt", "w")
    f.close()

    scraper.extract_new_links()
    
