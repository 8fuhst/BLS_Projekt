import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, CategoriesOptions, ConceptsOptions

with open("credentials.txt", "r") as credentials:
    api_key = credentials.readline()[:-1]  # removes the /n from the string
    api_url = credentials.readline()

# set up:
authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(api_url)


def prepare_and_generate_keywords(docnr, title, tenor_array, offense_array, reasons_array, reasonsfordecision_array):
    try:
        # generate keywords:
        result = defuse_response(
        generate_keywords(
        build_watson_query(title, tenor_array, offense_array, reasons_array, reasonsfordecision_array)))
    except:
        # in case of failure, adds ID of verdict to no_keywords.txt so that it can be retried at a later time
        result = []
        print("Generating keywords for " + docnr + " failed.")
        f = open("no_keywords.txt", "a")
        f.write(docnr + "\n")
        f.close()
    return result

def build_watson_query(title, tenor_array, offense_array, reasons_array, reasonsfordecision_array):
    """
    Creates the text from the verdict from which the keywords are generated:
    """
    tenor_array = ['{} '.format(elem) for elem in tenor_array]
    offense_array = ['{} '.format(elem) for elem in offense_array]
    reasons_array = ['{} '.format(elem) for elem in reasons_array]
    reasonsfordecision_array = ['{} '.format(elem) for elem in reasonsfordecision_array]
    if type(title) is list:
        title = "".join(title)
    result = title + "\n"
    result += "".join(tenor_array) + "\n"
    result += "".join(offense_array) + "\n"
    result += "".join(reasons_array) + "\n"
    result += "".join(reasonsfordecision_array)
    return result

def generate_keywords(text):
    """
    Generates Keywords for a given String by using the watson-natural-language-understanding API.
    Per execution this function uses 1 NLU Item, because the length of the input-text is cut to less
    than 10000 characters and the extracted feature is only ConceptsOptions.
    This results in 0.003 USD per execution(?).

    documentation:
    https://cloud.ibm.com/apidocs/natural-language-understanding?code=python#text-analytics-features
    pricing:
    https://www.ibm.com/cloud/watson-natural-language-understanding/pricing

    :param text: the text to be analysed
    :return: the generated keywords, the relevance (score) and the dbpedia_resource
    :rtype: list[dict{str: text, float: relevance, str: dbpedia_resource}]
    """
    # shortens text to meet the requirements for Watson NaturalLanguageUnderstanding
    if len(text) > 9500:
        text = text[:9500]
    response = natural_language_understanding.analyze(
        text=text,
        language="de",
        features=Features(concepts=ConceptsOptions(limit=10))).get_result()
    return json.dumps(response, indent=2)

# extract text from the Watson results:
def defuse_response(json_dict):
    json_dict = json.loads(json_dict)
    result = []
    for entry in json_dict["concepts"]:
        result.append(entry["text"])
    return result
