# Assignment - Prove it 01
# Demonstrates knowledge of variables, conditionals,
# and loops with the Number Guessing Game.
# I didn't understand the 'seed' thing at all or how
# to properly use functions to execute the play again.
# Jason Halverson explained and reviewed my code. He
# gently nudged me on how to correct my code.

import random
from random import randint
random.seed(the_seed_value) #Take care of the seed value

# declare the variables
number = random.randint(1, 100)
guess = int(input("Please enter a guess: "))
tries = 1

def game_intro():
    print("Welcome to the number guessing game!")
def get_random(number, guess, tries):
    random_seed = input("Enter random seed: ")
    random.seed(random_seed) 

    # Call functions
    guess_game(number, guess, tries)
    play_again(number, guess)

def guess_game(number, guess, tries):
    # Make a guessing loop using a while loop and IF statment
    while guess != number:
        if guess > number:
            print("Lower")
        else:
            print("Higher")
            guess = int(input("Please enter a guess: "))
            tries += 1
            print("Congratulations. You guessed it!")
            print("It took you", tries, "guesses.")

    def play_again(number, guess):
        # Use a WHILE LOOP to ask to play again
        while (play_again):
            guess_game(get_random)
            again = str(input("Would you like to play again (yes/no)? "))
            if again == no:
                
            if again == yes:
                guess_game(number, guess, tries)