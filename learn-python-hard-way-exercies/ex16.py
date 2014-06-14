# This is Exercise 16 : Reading and Writing Files

# Import "argv" module from "sys" packeges
from sys import argv

# Unpacking and assign value to variable
script, filename = argv

# Printing a sentence with filename
print "We're going to erase %r" % filename

# Printing a sentence and giving intruction.
print "If you don't want that, hit CTRL-C (^)"

# Printing another sentence
print "If you do want that, hit RETURN."

# Asking input form user
raw_input("?")

# Printing a sentence to open file
print "Opening the file..."

# A variable storing to open a file
target = open(filename, 'w')

# Printing a sentece and truncating the file.
print "Truncating the file. Goodbye!"

# Truncating the file 
target.truncate()

# Printing a sentence to ask 3 lines for input
print "Now I'm going to ask you for three lines."

# Asking first lines and storing in a variable
line1 = raw_input("line 1: ")

# Asking second lines and storing in a variable
line2 = raw_input("line 2: ")

# Asking third line and storing in a variable
line3 = raw_input("line 3: ")

# Printing a sentence saying writing the file
print "I'm going to write these to the file"

""" Note: Original code here

# Write line 1
target.write(line1)

# Writning new line by "\n"
target.write("\n")

# Write line2
target.write(line2)

# Add new line by "\n"
target.write("\n")

# Write line3
target.write(line3)

# Add new line by "\n"
target.write("\n")

"""

# Study Drill 3 : one  target.write() instead of six
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# Prinitng a sentece saying closing the file
print "And finally, we close it."

# close the file
target.close()

# Study Drill 2 : Read the file that you just created
# a variable to store file 
file = filename

# Open the file
open_file = open(file)

# Print the opened file
print open_file.read()
