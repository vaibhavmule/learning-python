# this is exercise 20 : Functions and Files

# import argv module from sys package
from sys import argv

# asking for argv
script, input_file = argv

# function that read file.
def print_all(f):

# print the file that read
	print f.read()

# function that seek
def rewind(f):

# print the file that seek
    f.seek(0)

# function that count the line
def print_a_line(line_count, f):

# print the line counted
	print line_count, f.readline()

# a variable that open the file
current_file = open(input_file)

# print a sentence 
print "First let's print the whole file: \n"

# print the file
print_all(current_file)

# print a sentence
print "Now let's rewind, kind of like a tape."

# rewind the file
rewind(current_file)

# print a sentence
print "Let's print three lines:"

# a variable that hold how many lines
current_line = 1

# call the function
print_a_line(current_line, current_file)

# a variable that hold variable with math expressions
current_line = current_line + 1

# call the function
print_a_line(current_line, current_file)

# overwriting the variable
current_line = current_line + 1

# call the function
print_a_line(current_line, current_file)

