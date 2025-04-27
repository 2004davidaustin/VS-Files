import random



def main():
    make_sentence(False, 0)
    make_sentence(False, 1)
    make_sentence(False, 2)
    make_sentence(True, 0)
    make_sentence(True, 1)
    make_sentence(True, 2)



def make_sentence(plural, tense):
    print(f"{get_prepositional_phrase(plural)}, {get_determiner(plural)} {get_adjective()} {get_noun(plural)} {get_verb(plural, tense)} {get_prepositional_phrase(plural)}.".capitalize())


def get_determiner(plural):
    determiners = ["a", "the", "one"]
    plural_determiners = ["two", "some", "many"]

    if plural : return random.choice(plural_determiners) 
    else : return random.choice(determiners)



def get_noun(plural):
    nouns = ["cat", "dog", "man", "woman", "girl", "boy", "child", "bird"]
    plural_nouns = ["cats", "dogs", "men", "friendly people", "foxes"]

    if plural : return random.choice(plural_nouns) 
    else : return random.choice(nouns)



def get_verb(plural, tense):
    past = ["ate", "ran", "thought", "wrote", "overcame"]
    present = ["eats", "runs", "thinks", "writes", "works hard"]
    present_plural = ["eat", "run", "think", "write", "become stronger"]
    future = ["will eat", "will run", "will think", "will write", "will become something great"]

    if tense == 0 : return random.choice(past)
    elif tense == 1 and plural : return random.choice(present_plural) 
    elif tense == 1 and not plural : return random.choice(present) 
    elif tense == 2 : return random.choice(future)



def get_prepositional_phrase(plural):
    preposition = get_preposition()
    determiner = get_determiner(plural)
    noun = get_noun(plural)

    if plural : return f"{preposition} {determiner} {noun}"
    else : return f"{preposition} {determiner} {noun}"


def get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
    return random.choice(prepositions)



def get_adjective():
    adjectives = ["happy", "sad", "angry", "excited", "bored",
      "tired", "hungry", "thirsty", "sick", "healthy",
      "strong", "weak", "smart", "dumb", "funny",
      "serious", "friendly", "mean", "kind", "rude"]
    return random.choice(adjectives)
    


main()