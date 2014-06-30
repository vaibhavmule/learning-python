# This is Exercise 11 : Asking Questions

# Printing a question asking for age
print "How old are you?",

# A variable storing an input of age
age = raw_input()

# Printing a question asking for height
print "How tall are you?",

# A variable storing an input of height
height = raw_input()

# Printing a question asking for weight
print "How much do you weigh",

# A variable storing an input of weight
weight = raw_input()

# After asking questions and getting answers, print a sentence using formatting
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)

