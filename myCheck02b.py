#---------------------------------------------------                                 
# Program:                                                                           
#    Checkpoint 02b, File Reading  
#    Brother Mellor, CS241                                                           
# Author:                                                                            
#    L Shamane Wells                                                                 
# Summary:                                                                           
#    Program reads an input file and counts the number of
#    words and lines. Practiced File Read syntax.                   
#    Got help from                                      
#---------------------------------------------------

#Prompt user for filename and return
def get_filename():
    filename = input("Enter file: ")
    return filename

#Accept filename parameter. Open file, then read
def read_file(filename):
    #Use file syntax: file_object = open(“filename”, “mode”)
    file = open(filename, "r")
    
    #Assign variables to 0
    word_count = 0
    line_count = 0
    
    #Use FOR LOOP to count each part of the file
    for line in file:
        line_count += 1
        words = line.split() #Syntax: a,b = x.split(“,”) USE A SPACE IN THIS INSTANCES
        word_count += len(words) 
    file.close() #Practice closing file 
    return(word_count, line_count)

#Driver program that calls the functions
def main():
   filename = get_filename()
   (word_count, line_count) = read_file(filename)
   print("The file contains", (line_count), "lines and", (word_count), "words.\n")

#tells program to start with the main function 
if __name__ == "__main__":
   main()
     