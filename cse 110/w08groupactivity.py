print("This is line one.", end="")
print("This is line two.")

word = "commitment"


'''

fav_letter = input("What's your favorite letter? ")

for i, letter in enumerate(word) : 
    if letter == fav_letter.lower() : print("_", end="")
    else : print(letter, end="")

'''



first_name = "Brigham"

# Notice by using enumerate, we specify both i and letter
for i, letter in enumerate(first_name):
    print(f"The letter {letter} is at position {i}")



text = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."


keepgoing = "yes"

while keepgoing.lower() == "yes" :

    number = int(input("What's your favorite number?? "))
    counter = 0

    for i, letter in enumerate(text) :
        counter += 1
        if counter == number :
            print(letter.upper(), end="")
            counter = 0
        else : print(letter.lower(), end="")
    print()

    keepgoing = input("Wanna put another number? (Yes/No) ")