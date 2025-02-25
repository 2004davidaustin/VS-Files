import random
continue_playing = "yes"



while "yes" in continue_playing :

    print("\nGuess the word!") 
    
    #word generator goes here
    word_chooser = ["word", "funny", "cool", "python"]
    word = word_chooser[random.randint(0, 3)]

    #reset variables
    guess = ""
    guess_count = 0
    display_word = ""

    while word != guess :
        guess_count += 1


        #display_selector = 0
        #while display_word[display_selector]  #hint machine
        
        
        guess = input("What's your guess? ").lower()
        
        if guess == word :
            print("YOU GOT IT!!!\n")
            print(f"You guessed: {guess_count} times")
            continue_playing = input("Wanna play again? (Yes or No) ").lower()
        else : print("Nope.")