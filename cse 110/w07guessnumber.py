import random
play = "yes"

while "yes" in play.lower() :
    print("\nGuess the number!")
    number = random.randint(1, 100)
    guess = -1
    guesses = 0
    while number != guess :
        guesses += 1
        guess = int(input("What's your guess? "))
        if guess > number : print("Lower...")
        if guess < number : print("Higher...")
        if guess == number :
            print("YOU GOT IT!!!\n")
            print(f"You guessed: {guesses} times")
            play = input("Wanna play again? (Yes or No) ")