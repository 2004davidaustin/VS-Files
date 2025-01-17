print("\n\n" + "Let's make a MadLib! Give me...")
animal = input("An animal: ")
verb1 = input("A verb: ")
verb2 = input("Another verb: ")
verb3 = input("Another another verb: ")
adj1 = input("An adjective: ")
adj2 = input("Another adjective: ")
adv = input("An adverb: ")
exclamation = input("An exclamation: ")
interjection = input("An interjection: ")

#Code from stack overflow
vowels = ("aieou")
if adj1[0].lower() in vowels:
    an = "an"
else:
    an = "a"

print(
f'''\n\nThe other day, I was really in trouble. It all started when I saw {an.lower()} {adj1.lower()} {animal.lower()} {verb1.lower()} down the hallway.
"{exclamation.upper()}!" I yelled. But all I could think to do was to {verb2.lower()} over and over.
Miraculously, that caused it to stop, but not before it tried to {adv.lower()} {verb3.lower()} right in front of my family.
{interjection.capitalize()}, I couldn't be more grateful that we made it out alive and {adj2.lower()}.\n\n'''
)