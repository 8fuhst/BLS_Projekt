import re

"""
Is used to convert the Tenor into a suitable format for further analysis.
"""

date_dict = {
    '01': 'Januar',
    '02': 'Februar',
    '03': 'März',
    '04': 'April',
    '05': 'Mai',
    '06': 'Juni',
    '07': 'Juli',
    '08': 'August',
    '09': 'September',
    '10': 'Oktober',
    '11': 'November',
    '12': 'Dezember'
}

def replace_abbreviations(text):
    return replace_punctuation_marks(replace_number_formats(replace_dates(text)))

def replace_punctuation_marks(text):
    text.replace("a. ", " am ")
    text.replace("1. ", "1_ ")
    text.replace("2. ", "2_ ")
    text.replace("3. ", "3_ ")
    text.replace("4. ", "4_ ")
    text.replace("5. ", "5_ ")
    text.replace("6. ", "6_ ")
    text.replace("7. ", "7_ ")
    text.replace("8. ", "8_ ")
    text.replace("9. ", "9_ ")
    text.replace("i.V.m.", "in Verbindung mit")
    text.replace("VIII.", "VIII_")
    text.replace("VII.", "VII_")
    text.replace("XII.", "XII_")
    text.replace("III.", "III_")
    text.replace("II.", "II_")
    text.replace("XI.", "XI_")
    text.replace("IX.", "IX_")
    text.replace("VI.", "VI_")
    text.replace("IV.", "IV_")
    text.replace("V.", "V_")
    text.replace("I.", "I_")
    text.replace("X. ", "10")
    text.replace("vgl. ", "vergleiche ")
    text.replace("Abs. ", "Absatz ")
    text.replace("Art. ", "Artikel ")
    text.replace("Nr. ", "Nummer ")
    text.replace("(vgl. ", "(vergleiche ")
    text.replace("(Abs. ", "(Absatz ")
    text.replace("(Art. ", "(Artikel ")
    text.replace("(Nr. ", "(Nummer ")
    text.replace("Prof.", "Professor")
    text.replace("Dr.", "Doktor")
    text.replace("bzw.", "beziehungsweise")
    text.replace("z. B.", "zum Beispiel")
    text.replace("z.B.", "zum Beispiel")
    text.replace("Buchst.", "Buchstabe")
    text.replace(" S.", " Seite")
    text.replace(" s.", " Seite")
    text.replace("\f", "")
    text.replace("Az.", "Aktenzeichen")
    text.replace("\n", "")
    return text


# 01.01.1999 -> 1 Januar 1999
def replace_dates(text):
    pattern = re.compile("\d{2}\\.\d{2}\\.\d{4}") # Todo: weitere Datumsformate?
    matches = re.findall(pattern, text)
    result = ""
    for match in matches:
        split = match.split('.')
        result = "{} {} {}".format(split[0], date_dict[split[1]], split[2])
        result = text.replace(match, result)
    return result


def replace_number_formats(text):
    pattern = re.compile("\d\\.\\d")
    matches = re.findall(pattern, text)
    for match in matches:
        new = match.replace(".", "")
        text = text.replace(match, new)
    return text