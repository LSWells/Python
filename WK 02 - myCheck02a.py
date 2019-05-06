# Checkpoint 02A
# Program prompts user for 3 postive numbers, then adds them.
# Practice syntax for creating functions and passing parameters.
# Got help from instructor's comments on SLACK 

#Create function, must prompt for number and ensure its positive
# Prompt for a positive number from the user.
def prompt_number():
   num = -1 #DECLARE VARIBLE
   while num < 0:
      num_str = input("Enter a positive number: ") #USE STR
      num = int(num_str) #TURN TO INT
      if num < 0:
         print("Invalid entry. The number must be positive.")
   return num #return value to MAIN to be PRINT
    
#Create function, accepts 3 numbers and returns sum
def compute_sum(num1, num2, num3):
    sum = (num1 + num2 + num3) #Add values and assign to sum
    return sum
    #End of function

#Main function, driver to call functions and save values
def main():
    #Call prompt function 3 times and assign to variable
    num1 = prompt_number()
    print()
    num2 = prompt_number()
    print()
    num3 = prompt_number()
    print()
    total = compute_sum(num1, num2, num3)
    print("The sum is:", (total))

#tells program to start with the main function
if __name__ == "__main__":
    main()