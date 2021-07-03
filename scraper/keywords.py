import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions, CategoriesOptions, ConceptsOptions

with open("./credentials.txt", "r") as credentials:
    api_key = credentials.readline()[:-1]  # removes the /n from the string
    api_url = credentials.readline()

authenticator = IAMAuthenticator(api_key)
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

natural_language_understanding.set_service_url(api_url)

def prepare_and_generate_keywords(title, tenor_array, offense_array, reasons_array, reasonsfordecision_array):
    return defuse_response(
        generate_keywords(
        build_watson_query(title, tenor_array, offense_array, reasons_array, reasonsfordecision_array)))

def build_watson_query(title, tenor_array, offense_array, reasons_array, reasonsfordecision_array):
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
    if len(text) > 9500:
        text = text[:9500]
    response = natural_language_understanding.analyze(
        text=text,
        language="de",
        features=Features(concepts=ConceptsOptions(limit=10))).get_result()
        #features=Features(categories=CategoriesOptions(limit=3))).get_result()
        # features=Features(keywords=KeywordsOptions(sentiment=False, emotion=False, limit=30))).get_result()
    return json.dumps(response, indent=2)

def defuse_response(json_dict):
    json_dict = json.loads(json_dict)
    result = []
    for entry in json_dict["concepts"]:
        result.append(entry["text"])
    return result

title_str = "Nichtannahmebeschluss: Erfolglose Verfassungsbeschwerde gegen Begrenzung des Kreises der \"Genesenen\" gemäß § 2 COVID-19-Schutzmaßnahmen-Ausnahmeverordnung (juris: SchAusnahmV) - Bundesrechtliche Beschränkung auf Personen mit positivem Test innerhalb der letzten sechs Monate betrifft Beschwerdeführer nicht mehr - mangelnde Rechtswegerschöpfung hinsichtlich vergleichbarer landesrechtlicher Vorschrift"
reasons_str = ["I.","1","Der Beschwerdeführer war Ende März 2020 mit dem Coronavirus SARS-CoV-2 infiziert. Mit seiner am 26. Mai 2021 erhobenen Verfassungsbeschwerde macht er eine Verletzung seiner Grundrechte aus Art. 3 Abs. 1 und Art. 2 Abs. 1 GG durch die COVID-19-Schutzmaßnahmen-Ausnahmenverordnung (SchAusnahmV) geltend. Er beanstandet eine unzulässige Ungleichbehandlung. Personen deren nachgewiesene Infektion mit dem Coronavirus, wie bei dem Beschwerdeführer, schon mehr als sechs Monate zurückliegt, gelten nach § 2 Nr. 4 und 5 SchAusnahmV im Unterschied zu solchen, bei denen die nachgewiesene Infektion mit dem Coronavirus weniger als sechs Monate zurückliegt, nicht als genesene Personen. Für den Beschwerdeführer kommen deshalb die Ausnahmen nach der Schutzmaßnahmen-Ausnahmenverordnung nicht zur Anwendung. Daran ändert auch nichts, dass er nach wie vor über ausreichend neutralisierende Antikörper gegen das Coronavirus im Blut verfügt und das mittels eines aktuellen Nachweises auch belegen kann. Der Beschwerdeführer sieht sich auch dadurch benachteiligt, dass er nicht durch lediglich eine Impfung den Status einer geimpften Person erreichen könne (vgl. § 2 Nr. 3 lit. b SchAusnahmV), weil auch dies voraussetze, genese Person zu sein und damit wiederum erfordere, dass die Infektion nicht länger als sechs Monate zurückliege."
    ,"2","§ 2 Nr. 2 bis 5 SchAusnahmV hat folgenden Wortlaut:","§ 2 Begriffsbestimmungen","Im Sinne dieser Verordnung ist","[…]","2. eine geimpfte Person eine asymptomatische Person, die im Besitz eines auf sie ausgestellten Impfnachweises ist,","3. ein Impfnachweis ein Nachweis hinsichtlich des Vorliegens einer vollständigen Schutzimpfung gegen das Coronavirus SARS-CoV-2 in deutscher, englischer, französischer, italienischer oder spanischer Sprache in verkörperter oder digitaler Form, wenn die zugrundeliegende Schutzimpfung mit einem oder mehreren vom Paul-Ehrlich-Institut im Internet unter der Adresse www.pei.de/impfstoffe/covid-19 genannten Impfstoffen erfolgt ist, und","a) entweder aus einer vom Paul-Ehrlich-Institut im Internet unter der Adresse www.pei.de/impfstoffe/covid-19 veröffentlichten Anzahl von Impfstoffdosen, die für eine vollständige Schutzimpfung erforderlich ist, besteht und seit der letzten erforderlichen Einzelimpfung mindestens 14 Tage vergangen sind oder","b) bei einer genesenen Person aus einer verabreichten Impfstoffdosis besteht,","4. eine genesene Person eine asymptomatische Person, die im Besitz eines auf sie ausgestellten Genesenennachweises ist,","5. ein Genesenennachweis ein Nachweis hinsichtlich des Vorliegens einer vorherigen Infektion mit dem Coronavirus SARS-CoV-2 in deutscher, englischer, französischer, italienischer oder spanischer Sprache in verkörperter oder digitaler Form, wenn die zugrundeliegende Testung durch eine Labordiagnostik mittels Nukleinsäurenachweis (PCR, PoC-PCR oder weitere Methoden der Nukleinsäureamplifikationstechnik) erfolgt ist und mindestens 28 Tage sowie maximal sechs Monate zurückliegt,","[…]","II.","3","Die Verfassungsbeschwerde ist unzulässig.","4","1. Der Beschwerdeführer hat nicht dargelegt, dass er von bundesrechtlichen Beschränkungen (§ 28b IfSG) aktuell betroffen ist. Soweit ersichtlich, lagen deren Voraussetzungen am Wohnort des Beschwerdeführers im Zeitpunkt der Erhebung der Verfassungsbeschwerde nicht mehr vor. Insofern betrifft ihn auch die hier angegriffene Ausnahmeregelung nicht mehr. Ob der Beschwerdeführer hinreichend dargelegt hat, aktuell durch Beschränkungen des Landesrechts Berlins und damit wenigstens insoweit von der nach § 7 Abs. 1 SchAusnahmV auch hier geltenden Ausnahmeregelung betroffen zu sein, kann dahinstehen, weil die Verfassungsbeschwerde insofern aus anderem Grund unzulässig ist.","5","2. Sofern der Beschwerdeführer dadurch gegenwärtig betroffen sein könnte, dass die in der Schutzmaßnahmen-Ausnahmenverordnung geregelten Ausnahmen von aktuellen Beschränkungen des Landesrechts für ihn nicht gelten, weil seine Infektion mehr als sechs Monate zurückliegt, genügt die Verfassungsbeschwerde nicht den Anforderungen der Subsidiarität.","6","a) Der Grundsatz der Subsidiarität erfordert grundsätzlich, vor Einlegung einer Verfassungsbeschwerde alle zur Verfügung stehenden prozessualen Möglichkeiten zu ergreifen, um eine Korrektur der geltend gemachten Verfassungsverletzung zu erwirken oder eine Grundrechtsverletzung zu verhindern. Hier kommt verwaltungsgerichtlicher Rechtsschutz in Betracht. Zwar bedarf es keiner vorangehenden fachgerichtlichen Entscheidung, wenn eine Norm zur Überprüfung steht und die Beurteilung einer Norm allein spezifisch verfassungsrechtliche Fragen aufwirft, die das Bundesverfassungsgericht zu beantworten hat, ohne dass von einer vorausgegangenen fachgerichtlichen Prüfung verbesserte Entscheidungsgrundlagen zu erwarten wären (vgl. zur Verfassungsbeschwerde gegen ein Gesetz BVerfGE 150, 309 <327 Rn. 44> m.w.N.; stRspr). Das ist hier jedoch nicht der Fall.","7","b) Das Landesrecht von Berlin enthält zu der hier streitigen Frage eine großzügigere Regelung als der teilweise angegriffene § 2 SchAusnahmV. Nach § 6c Abs. 1 Nr. 2der Zweiten SARS-CoV-2-Infektionsschutzmaßnahmenverordnungdes Landes Berlin (Zweite SARS-CoV-2-Infektionsschutzmaßnahmenverordnung <2. InfSchMV>) entfällt eine nach dieser Verordnung oder nach § 28b IfSG vorgeschriebene Pflicht, negativ auf eine Infektion mit dem Coronavirus SARS-CoV-2 getestet zu sein oder ein negatives Testergebnis einer mittels anerkannten Tests durchgeführten Testung auf eine Infektion mit dem Coronavirus SARS-CoV-2 vorlegen zu müssen, für genesene Personen, die ein mehr als sechs Monate zurückliegendes positives PCR-Testergebnis auf eine Infektion mit dem Coronavirus SARS-CoV-2 nachweisen können und die mindestens eine Impfung gegen Covid-19 mit einem von der Europäischen Union zugelassenen Impfstoff erhalten haben und deren Impfung mindestens 14 Tage zurückliegt. Nach § 6c Abs. 1 Nr. 2 der 2. InfSchMV könnte der Beschwerdeführer also aufgrund seiner früheren Infektion bereits durch lediglich eine Schutzimpfung in den Genuss der genannten Befreiungen kommen. Dass die Infektion mehr als sechs Monate zurück liegt, steht dem nach § 6c Abs. 1 Nr. 2 der 2. InfSchMV ‒ anders als nach § 2 Nr. 3 lit. b SchAusnahmV ‒ nicht entgegen.","8","Der Beschwerdeführer ist allerdings der Ansicht, die Regelung des Landesrechts sei nach Art. 31 GG nichtig. Dies schließt er aus § 7 Abs. 1 SchAusnahmV. Die Vorschrift regelt, dass sofern auf Grund der Vorschriften des fünften Abschnitts des Infektionsschutzgesetzes erlassenes Landesrecht eine Ausnahme von Geboten oder Verboten für Personen vorgesehen ist oder erlassen wird, die negativ auf eine Infektion mit dem Coronavirus SARS-CoV-2 getestet sind, diese Ausnahme auch für geimpfte Personen und genesene Personen gilt. Es ist jedoch eine Frage näherer Auslegung des einfachen Rechts, ob § 7 Abs. 1 in Verbindung mit § 2 SchAusnahmV einer Landesregelung entgegensteht oder nicht, die wie § 6c Abs. 1 Nr. 2 der 2. InfSchMV für den Anwendungsbereich landesrechtlicher Beschränkungen die Begriffe der genesenen oder der geimpften Person großzügiger fasst als § 2 Nr. 3 lit. b SchAusnahmV. Wenn die großzügigere Regelung des § 6c Abs. 1 Nr. 2 der 2. InfSchMV anwendbar ist, könnte der Beschwerdeführer bereits durch lediglich eine Schutzimpfung in den Genuss der Befreiungen von aktuellen landesrechtlichen Beschränkungen kommen. Sollte die Auslegung des Fachrechts ergeben, dass § 7 Abs. 1 in Verbindung mit § 2 SchAusnahmV großzügigeren Ausnahmen von landesrechtlichen Beschränkungen nicht entgegenstehen, könnte der Beschwerdeführer auch sein Begehren, über § 6c Abs. 1 Nr. 2 der 2. InfSchMV hinaus ohne jede weitere Impfung in den Genuss der Befreiungen zu kommen, auf der Grundlage des Landesrechts im Wege des verwaltungsgerichtlichen Rechtsschutzes durchzusetzen versuchen.","9","Von einer weiteren Begründung wird nach § 93d Abs. 1 Satz 3 BVerfGG abgesehen.","10","Diese Entscheidung ist unanfechtbar."]
tenor_str = ["1. Die Verfassungsbeschwerde wird nicht zur Entscheidung angenommen.","2. Mit der Nichtannahme der Verfassungsbeschwerde wird der Antrag auf Erlass einer einstweiligen Anordnung gegenstandslos (§ 40 Abs. 3 GOBVerfG)."]
offense_str = []
reasonsfordecision_str = []

#response = generate_keywords(build_watson_query(title_str, tenor_str, offense_str, reasons_str, reasonsfordecision_str))

#print(response)
#print(defuse_response(response))
