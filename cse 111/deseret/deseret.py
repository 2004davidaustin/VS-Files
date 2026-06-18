# py -m pip install eng-to-ipa

import eng_to_ipa as ipa
import re

"""

Resources used:

https://en.wikipedia.org/wiki/Deseret_alphabet
https://elliotec.com/writing-in-the-deseret-alphabet/
https://pypi.org/project/eng-to-ipa/#description
http://www.speech.cs.cmu.edu/cgi-bin/cmudict
https://www.2deseret.com/
https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
https://en.wikipedia.org/wiki/Phoneme#Notation
https://ipa-reader.com/
https://easypronunciation.com/en/american-english-pronunciation-ipa-chart
https://tophonetics.com/


"""





def main():

    choice = -1

    while choice != 0 :

        #print options
        print()
        print("Translate Text to...")
        print("1 | Complete IPA")
        print("2 | Manual IPA")
        print("3 | Deseret")
        print("0 | Quit")
        choice = int(input())
        print()
        if choice != 0 : 
            text = input("Input your text\n")
            print()

        #print chosen option
        if choice == 1 :
            print(to_ipa(text))
        elif choice == 2 :
            print(ipa_fallback(text))
        elif choice == 3 :
            print(ipa_to_deseret(to_ipa(text)))
        elif choice == 0 :
            print("ˌoʊˈkeɪ, baɪ!\n")

    pass














# CONVERT TEXT TO IPA and use fallback for unknown words

def to_ipa(original_text):

    # eng to ipa thing
    converted_text = ipa.convert(original_text)

    #print("\n" + converted_text) # TESTING TESTING TESTING





    # find unchanged words and use ipa_fallback to change them
    asterisk_words = re.findall(r"\b([^\s*]+)\*", converted_text)

    for word in asterisk_words: 
        
        # generate new ipa with fallback
        replacement = ipa_fallback(word)
        # Replace ONLY that specific instance
        converted_text = re.sub(rf"\b{word}\*", replacement, converted_text, count=1)

        print(f"Found {word}, replaced with {replacement}") # TESTING TESTING TESTING

    #print("\n" + converted_text) # TESTING TESTING TESTING





    return converted_text







DIGRAPHS = {
    # vowel digraphs
    "ai":"eɪ", "ay":"eɪ", "ei":"eɪ", "ey":"eɪ",
    "au":"ɔ", "aw":"ɔ",
    "ea":"i", "ee":"i", "ie":"i",
    "ew":"ju",
    "oa":"oʊ", "oe":"oʊ",
    "oi":"ɔɪ", "oy":"ɔɪ",
    "oo":"u",
    "ou":"aʊ", "ow":"aʊ",
    "ua":"ua",
    "ue":"ju", "ui":"ju",

    # vowels with r
    "ar":"ɑr", "or":"ɔr", "er":"ər", "ir":"ər", "ur":"ər",

    # consonant digraphs
    "ch":"ʧ", "tch":"ʧ", "sh":"ʃ", "th":"θ", "ph":"f", "ng":"ŋ", "ck":"k", "zh":"ʒ", "kn":"n", "wr":"r", "dge":"ʤ", "qu":"kw", "igh":"aɪ", "gh":"g",

    #double consonants
    "bb":"b", "cc":"k", "dd":"d", "ff":"f", "gg":"g", "kk":"k", "ll":"l", "mm":"m", "nn":"n", "pp":"p", "rr":"r", "ss":"s", "tt":"t", "zz":"z",

    #strange vowel+l effect
    "al":"ɔl", "ol":"oʊl",

    # soft sounds
    "ce":"sɛ", "ci":"sɪ", "cy":"saɪ",
    "ge":"ʤɛ", "gi":"ʤaɪ", "gy":"ʤɪ"
}

FINAL_RULES = {

    "ization": "aɪzeɪʃən",
    "zation": "zeɪʃən",
    "xion": "kʃən",
    "tion": "ʃən",
    "sion": "ʒən",
    "cian": "ʃən",
    "tial": "ʃəl",
    "cial": "ʃəl",
    "tian": "ʃən",

    "tious": "ʃəs",
    "cious": "ʃəs",
    "ious":  "jəs",
    "eous":  "iəs",
    "uous":  "juəs",

    "ing":"ɪŋ",
    "le":"l", "mb":"m", "bt":"t",
    "e":"i", "i":"aɪ", "o":"oʊ", "y":"i"
}

SINGLE = {
    "a":"æ", "b":"b", "c":"k", "d":"d", "e":"ɛ", "f":"f", "g":"g", "h":"h",
    "i":"ɪ", "j":"ʤ", "k":"k", "l":"l", "m":"m", "n":"n", "o":"ɒ", "p":"p",
    "q":"k", "r":"r", "s":"s", "t":"t", "u":"ʌ", "v":"v", "w":"w", "x":"ks",
    "y":"j", "z":"z"
}

IPA_TO_GLYPH = {
    "i":"𐐀",    "oʊ":"𐐄",   "æ":"𐐈",    "aɪ":"𐐌",   "h":"𐐐",    "d":"𐐔",
    "ɡ":"𐐘",    "ð":"𐐜",    "ʒ":"𐐠",    "n":"𐐤",    "eɪ":"𐐁",    "u":"𐐅",
    "ɒ":"𐐉",    "aʊ":"𐐍",    "p":"𐐑",    "ʧ":"𐐕",    "f":"𐐙",    "s":"𐐝",
    "r":"𐐡",    "ŋ":"𐐥",    "ɑ":"𐐂",    "ɪ":"𐐆",    "ʌ":"𐐊",    "w":"𐐎",
    "b":"𐐒",    "ʤ":"𐐖",    "v":"𐐚",    "z":"𐐞",    "l":"𐐢",    "ɔɪ":"𐐦",
    "ɔ":"𐐃",    "ɛ":"𐐇",    "ʊ":"𐐋",    "j":"𐐏",    "t":"𐐓",    "k":"𐐗",
    "θ":"𐐛",    "ʃ":"𐐟",    "m":"𐐣",    "ju":"𐐧",

    "ə":"𐐇"
}


# IPA FALLBACK CLEANS THE TEXT, SPLITS IT INTO WORDS, PROCESSES EACH WORD, AND RETURNS IT

def ipa_fallback(text):
    # Split into words and punctuation
    tokens = re.findall(r"\b[\w']+\b|[^\w\s]", text)
    results = []
    
    for token in tokens:
        if re.match(r"[\w']+", token):  # It's a word
            # Remove apostrophes from the word before processing
            clean_token = token.replace("'", "")
            results.append(word_to_ipa(clean_token))
        else:  # It's punctuation
            results.append(token)
    
    return " ".join(results)



# WORD TO IPA
# the reason why there's a specific function the 
# individual words and not the whole text is because 
# some words have weird endings and this is supposed 
# to deal with that

def word_to_ipa(word):

    w = word.lower()
    i = 0
    out = []
    
    while i < len(w):
        
        # END-OF-WORD RULES
        matched = False
        for ending, ipa in sorted(FINAL_RULES.items(), key=lambda x: -len(x[0])):
            if w[i:].endswith(ending) and len(w[i:]) == len(ending):
                out.append(ipa)
                i += len(ending)
                matched = True
                break
        if matched:
            continue


        # SILENT E RULE
        if i+3 <= len(w) and w[i] in "aeiou" and w[i+2] == "e":

            #print("silet e rule used!", w[i:i+3]) # TESTING TESTING TESTING

            out.append({
                'a':'eɪ',
                'i':'aɪ',
                'o':'oʊ',
                'u':'u',
                'e':'i'
            }[w[i]])
            i += 1

            #replace letter before e (including added silent e rule) and move forward two skipping the e
            if w[i] == "c" : out.append("s")
            elif w[i] == "g" : out.append("ʤ")
            else : out.append(SINGLE.get(w[i], w[i]))
            i += 2

            continue


        # 3-letter digraph
        if i+3 <= len(w) and w[i:i+3] in DIGRAPHS:
            out.append(DIGRAPHS[w[i:i+3]])
            i += 3
            continue


        # 2-letter digraphs
        if i+2 <= len(w) and w[i:i+2] in DIGRAPHS:
            out.append(DIGRAPHS[w[i:i+2]])
            i += 2
            continue

            
        # Single letter fallback
        out.append(SINGLE.get(w[i], w[i]))
        i += 1
        

        #print(out) # TESTING TESTING TESTING

    return "".join(out)



# IPA TO DESERET CODE

# Sort keys by length so longer IPA symbols are matched first
IPA_PAT = re.compile("|".join(sorted(IPA_TO_GLYPH, key=len, reverse=True)))

def ipa_to_deseret(ipa_text):

    #get rid of ˈ and ˌ because I don't need or want them
    cleaned_text = re.sub(r"[ˈˌ]", "", ipa_text)
    #print("\n" + cleaned_text) # TESTING TESTING TESTING

    return IPA_PAT.sub(lambda m: IPA_TO_GLYPH[m.group(0)], cleaned_text)








 









#cool other things

'''
def read_json(file):
    
    data = []
    with open(file, "r", encoding="utf8") as f:
        for line in f:
            data.append(json.loads(line))

    return data



def print_list(list):

    #print each line
    for line in list:

        # map allows us to edit each variable in the line array variable
        # lambda returns the individual word + the remaining spaces necessary to make 14 spaces so the words are evened out
        # join spits out the iterable as a string with "" inbetween each variable in the array
        print("".join(map(lambda word: word + " " * (14 - len(word)), line)))

'''

if __name__ == "__main__":
    main()