# This is Exercise 6 : Strings and Text

# Variable including how many type of people with sentence.
x = "There are %d types of people." % 10

# Store strings in Variable
binary = "binary"

# Again store strings in variable.
do_not = "don't"

# Store a sentence with above two variables in variable.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print a sentence of type of people as variable
print x

# Print a sentence which stored in variable
print y

# Print a sentence with varibel which stored sentence but using formatting
print "I said: %r" % x

# Again print another sentence with variable which stored sentence but using formatting
print "I also said: '%s'." %y

# Create Boolean 
hilarious = False

# Store a sentence in a variable with formatting
joke_evaluation = "Isn't that joke so funny?! %r" # Here %r is used for debuging.

# Print Boolean and sentence which including formatting in a variable
print joke_evaluation % hilarious

# Create a variable including a sentence
w = "This is the left side of..."

# Again create a variable including a sentence
e = "a string with a right side."

# Print above two variables which includes sentences using '+' concatnation
print w + e 