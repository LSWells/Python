# WK 01 Prove Assignment
# L Shamane Wells
# McKay Murphy assisted me with the
# random seed and the play again feature.

import random

print("Welcome to the number guessing game!")
random_seed = input("Enter random seed: ")
random.seed(random_seed)
play_again = "yes"

while play_again == "yes":
    number = random.randint(1, 100)
    guess = int(input("Please enter a guess: "))
    tries = 1

    while guess != number:
        if guess > number:
            print("Lower")
        else:
            print("Higher")
            
        guess = int(input("Please enter a guess: "))
        tries += 1

    print("Congratulations. You guessed it!")
    print("It took you", tries, "guesses.\n")

    play_again = (input("Would you like to play again (yes/no)? "))
        

    
            
