#import argv from library
from sys import argv

#initialise variables for argument variable
script, filename = argv

#call the open function to open the file in argv and assign it to txt
#txt = open(filename)

#print name of file|| call the read function on txt where file is assigned and print it
#print (f"Here's your file {filename}:")
#print (txt.read())

#assign the input value from user to file_again
print ("Type the filename again:")
file_again = input("> ")

#open file_again and assign it to txt_again
txt_again = open(file_again)

#call read function on txt_again and print the output
print (txt_again.read())
