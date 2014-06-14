# this is exercise 21: Functons can return something

# a function that do addition
def add(a, b):

# a sentence saying what you are adding
	print "ADDING %d + %d" % (a, b)

# return the value
	return a + b

# a function that to do subtraction
def subtract(a, b):

# a sentence saying what you are subtracting
	print "SUBTRACTION %d - %d" % (a, b)

# return the value
	return a - b

# a function that multiplu numbers
def multiply(a, b):

# a sentence saying what you are multiplying
	print "MULTIPLYING %d * %d" % (a, b)

# return the value 
	return a * b

# a functoin that divide
def divide(a, b):

# a sentence saying what you are dividing 
	print "DIVIDING %d / %d" % (a, b)

# return the value
	return a / b

# print the sentence
print "Let's do some math with just fractions!"

# a variable that hold function callback of addtion
age = add(30, 5)

# a variable which hold function callback of subtraction
height = subtract(78, 4)

# a variable which hold function callback of multiplication
weight = multiply(90, 2)

# a varible which divide
iq = divide (100, 2)

# print a sentence including +, - , * , /
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it anyway
# print a sentence
print "Here is a puzzle"

# a variable storing mathematical expression
what = add(age, subtract(height, multiply(weight, divide (iq, 2))))

# print a sentence wiht answer of above expression
print "That becomes: ", what, "Can you do it by hand?"
