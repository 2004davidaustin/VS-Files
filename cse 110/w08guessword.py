import random
continue_playing = "yes"



#online word bank downloader
import urllib3
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib3.request("GET", word_site)
site_words = response.data.splitlines()

#only use 3-5 letter words from the online list and decode them
word_bank = []
for s in site_words :
    if 3 <= len(s) <= 5 : word_bank.append(s.decode("utf-8"))



#'''
while "yes" in continue_playing :
    #start and reset variables
    print("\nGuess the word!")
    guess = ""
    guess_count = 0



    #word generator
    word = word_bank[random.randint(0, len(word_bank))]

    #initial hint
    for i in enumerate(word) :
        print("_", end=" ")
    print()



    while word != guess :
        guess_count += 1
        
        guess = input("What's your guess? ").lower()

        #cheat
        if guess == "helpme" : print(word)



        #length verifier
        while len(word) != len(guess) :
            print("Guess length must match word length")
            guess = input("What's your guess? ").lower()
        


        #guess checker
        if guess == word :
            print("\nYOU GOT IT!!!")
            print(f"You guessed: {guess_count} times")
            continue_playing = input("Wanna play again? (Yes or No) ").lower()
        else :

            #hint machine
            for i, letter in enumerate(word) :
                if letter in guess and letter == guess[i] : print(letter.upper(), end=" ")
                elif letter in guess : print(letter, end=" ")
                else : print("_", end=" ")
            print()

            print("Nope.\n")
#'''