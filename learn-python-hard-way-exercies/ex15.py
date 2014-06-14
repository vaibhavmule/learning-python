# This is Exercise 15: Reading Files

# Import sys modules and argv is an argument variable
# which holds arguments that you pass on Pyhton script
from sys import argv

# Unpacking and assing value to variables
script, filename = argv

# A variable storing function to open file.
txt = open(filename)

# Printing a sentence saying filename
print "Here's your file %r:" % filename

# Printing a function to read file
print txt.read()

# Printing a sentence to read file again
print "Type the filename again:"

# A variable asking input
file_again = raw_input("> ")

# A variable to open a file
txt_again = open(file_again)

# A variable to read file
print txt_again.read() 