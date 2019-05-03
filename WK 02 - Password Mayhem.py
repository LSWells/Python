# Password
# Demonstrates the IF statement

print("Welcome to System Security Inc.")
print("-- where security is our middle name")
print("   and privacy is nothing but an illustion. \n")

password = input("Enter your password that will be public by the end of the day: ")

if password == "secret":
    print("Access Granted.")
    print("Thank you for sharing your private information.")
else:
    print("Access Denied.")
    print("You are attempting to select a secure password.")
    print("System Security cannot allow unique passwords that will impede absolute control.")
    