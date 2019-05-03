# DnD Roller
# Demonstrates random number generation

import random

# Generate random numbers 1 - 20.
# Below are two didn't ways for generating a number

die1 = random.randint(1, 20)
die2 = random.randrange(20) + 1 #randrange starts at 0!

total = die1 + die2

print("A troll stands in your path, and swing a large branch at your head.")
print("Roll the dice to evade the troll's attack, any roll below a 10 and the trolls attack hit you.") 
print("\n\nYou rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress the enter key to exit.")