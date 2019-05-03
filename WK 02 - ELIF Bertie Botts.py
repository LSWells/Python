# Mood Computer
# Demonstrate the ELIF clause thought mood enhancers.

import random

print("Welcome to Harry Potter World, please stop by and")
print("try one of Bertie Botts' Every Flavour Beans!")
print("You have selected...")

bean = random.randint(1, 10)

if bean == 1:
    # Good Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  .     .  |
            |   `...'   |
            -------------
            """)
    print("Tutti-Frutti! You lucky duck!")
elif bean == 2:
    # Good Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  .     .  |
            |   `...'   |
            -------------
            """)
    print("Candyfloss! Be sure to try another one!")
elif bean == 3:    
        # Good Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  .     .  |
            |   `...'   |
            -------------
            """)
    print("Apple-Pie! An all-American treat!")
elif bean == 4:     
    # Meh Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  _______  |
            |           |
            -------------
            """)
    print("Banana. Not bad, gotta normal one!")
elif bean == 5:     
    # Meh Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  _______  |
            |           |
            -------------
            """)
    print("Mint! Could have been worse--way worse.")
elif bean == 6:     
    # Meh Flavor
    print( \
        """
            -------------
            |           |
            |   O   O   |
            |     <     |
            |  _______  |
            |           |
            -------------
            """)
    print("Coffee! No doubt that you needed the boost!")
elif bean == 7:
    # Yucky Flavor
    print( \
        """
            -------------
            |  __  __   |
            |   >   <   |
            |     <     |
            |  _______  |
            |    | | |  |
            |    |___|  |
            -------------
            """)
    print("Booger! Didn't your mother tell it not to eat those!")
elif bean == 8:
    # Yucky Flavor
    print( \
        """
            -------------
            |  __  __   |
            |   >   <   |
            |     <     |
            |  _______  |
            |    | | |  |
            |    |___|  |
            -------------
            """)
    print("Vomit! Looks like you'll be praying to the porcelain god!")
elif bean == 9:
    # Yucky Flavor
    print( \
        """
            -------------
            |  __  __   |
            |   >   <   |
            |     <     |
            |  _______  |
            |    | | |  |
            |    |___|  |
            -------------
            """)
    print("Dirty Socks! You poor schmuck! Your luck is awful!")
elif bean == 10:
    # Yucky Flavor
    print( \
        """
            -------------
            |  __  __   |
            |   >   <   |
            |     <     |
            |  _______  |
            |    | | |  |
            |    |___|  |
            -------------
            """)
    print("Earthworm! Gak! Don't forget to brush your teeth.")
else:
    print("Oh, you don't want to try a Bertie Bott's Bean? Coward!")
    print("Come back when you've mustered up bit of courage.")
    
   
input("\n\nPress the enter key to leave the shop.")    


