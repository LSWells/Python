#---------------------------------------------------
# Program:
#    Checkpoint 01b, Review
#    Brother Mellor, CS241
# Author:
#    L Shamane Wells
# Summary:
#    Showing off my brand new Python skills!
#    Comments can be left anywhere with the '#'
#---------------------------------------------------

n = input("Please enter your name: ")
a = int(input("Please enter your age: "))

# This prints out "Hello NAME, you are X years old.
#                  On your next birthday, you will be (X + 1)."
# %s, %r, %d are argument specifiers that will remove unwanted spacing.

print("\nHello %s," % n, "you are", a, "years old.")
print("On your next birthday, you will be %s." % (a + 1))

