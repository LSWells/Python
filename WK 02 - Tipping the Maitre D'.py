#Maitre D'
#Demonstrates treating a value as a condition

print("Welcome to the Chateau D' Food")
print("It seems we are quite full this evening. \n")

money = int(input("How many dollars do you slip the Maitre D'? "))

if money != 0:
    print("Ah, there seems to be a table. Please, right this way.")
else:
    print("Please, have a seat. It may be a while.")

input("\n\nPress the enter key to exit.")