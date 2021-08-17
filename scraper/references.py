import re

"""
Is used to search for References in an Array of Strings.
"""

aktenzeichenRegEx = re.compile("(((VGS|RiZ\s?s?\(R\)|KZR|VRG|RiZ|EnRB|StbSt\s?\(B\)|AnwZ\s?\(Brfg\)|RiSt|PatAnwSt\s?\(R\)|AnwZ\s?\(B\)|PatAnwZ|EnVZ|AnwSt\s?\(B\)|NotSt\s?\(Brfg\)|KVZ|KZB|AR\s?\(Ri\)|NotZ\s?\(Brfg\)|RiSt\s?\(B\)|AnwZ\s?\(P\)|EnZB|RiSt\s?\(R\)|NotSt\s?\(B\)|AnwSt|WpSt\s?\(R\)|KVR|AR\s?\(Kart\)|EnZR|StbSt\s?\(R\)|WpSt\s?\(B\)|KZA|AR\s?\(Enw\)|AnwSt\s?\(R\)|KRB|RiZ\s?\(B\)|PatAnwSt\s?\(B\)|EnVR|AnwZ|NotZ|EnZA|AR)\s\d+/\d+)|" \
                               # Spezielle-Akürzung Zahl/Zahl - Es gibt Aktenzeichen ohne Vorangehende (Römische)Zahl
                                "((GSZ|LwZB|WpSt\s?\(B\)|AnwZ|LwZR|KVZ|EnRB|PatAnwSt\s?\(B\)|ARP|VGS|WpSt\s?\(R\)|RiSt\s?\(B\)|EnZA|KRB|AnwSt\s?\(R\)|NotSt\s?\(Brfg\)|EnVR|LwZA|ZB|AR\s?\(Vollz\)|StB|ZR|AR\s?\(VS\)|BJs|BLw|NotZ\s?\(Brfg\)|RiZ\s?\(B\)|PatAnwSt\s?\(R\)|AK|RiZ|PatAnwZ|ARs|StbSt\s?\(R\)|VRG|NotSt\s?\(B\)|AR\s?\(Enw\)|AR\s?\(VZ\)|StE|KVR|AR\s?\(Ri\)|AR|AnwSt|NotZ|StbSt\s?\(B\)|StR|ZA|AnwZ\s?\(B\)|EnZR|AR\s?\(Kart\)|GSSt|AnwZ\s?\(P\)|ZR\s?\(Ü\)|AnwZ\s?\(Brfg\)|KZB|BGns|KZR|RiSt|KZA|BAusl|AnwSt\s?\(B\)|BGs|RiZ\s?\(R\)|EnZB|RiSt\s?\(R\)|ARZ|EnVZ)\s\d+/\d+)|" \
                                # Spezielle-Akürzung Zahl/Zahl - ähnlich zu Teil 1 inklusive Dopplungen der Abkürzungen...
                                "((?:I|II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|\d\d?)[a-z]?\s[A-Z][A-Za-z()]{,20}\s\d+/\d\d))")
                                # (Römische)Zahl(a-z) Kürzel Zahl/ZifferZiffer - Der wirklich relevante Teil todo: machen Klammern ohne mögliche Leerzeichen überhaupt Sinn in [A-Za-z()]?

def find_reference(text_array, outgoing_references_set):
    """
    Is used to search for references in an array of strings belonging to a verdict. Builds a list in the shape of
    [[1, Aktenzeichen, Aktenzeichen], [2, Aktenzeichen], [3, Aktenzeichen], ...]
    and adds new references to the reference-set of the current verdict.

    :param list(str) text_array: The string-array containing the to be examined text.
    :param set(str) outgoing_references_set: The current set, containing all previous found references for a verdict.

    :return: A dict containing the tag as key and the found references as a list, and the updated references-set
    :rtype: dict(str: list(str)) and set(str)
    """
    matches_dict = {}
    all_matches = {}
    index_dict = {}
    index_matches_list = []
    for index, text in enumerate(text_array):
        # find the reference matches of a sentence:
        matches = re.findall(aktenzeichenRegEx, text)
        for match in matches:
            for entry in match:
                if entry != '':
                    # add each reference with its line to the dict:
                    index_dict["index"] = index
                    index_dict["referenz"] = entry
                    outgoing_references_set.add(entry)
                    if not index_dict in index_matches_list: # prevent duplicates
                        index_matches_list.append(index_dict.copy())

    return index_matches_list, outgoing_references_set
