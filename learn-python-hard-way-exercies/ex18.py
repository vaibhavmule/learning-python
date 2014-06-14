# This is Exercise 18 : Names, Variables, Code, Funcions

# this one is like your script with argv
def print_two(*args):

# two argv is equal to one argv
	arg1, arg2 = args

# print both argv
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can to this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
# create funciton with one argument
def print_one(arg1):

# print the argument
	print "arg1: %r" % (arg1)

# this one takes no arguments
# create function with no arguments
def print_none():

# print the argument in function
	print "I got nothin'."

# Callback functions with two argument
print_two("Vaibhav", "Mule")

# Again Callback function with two argument
print_two_again("Vaibhav", "Mule")

# Callback the function with one argument
print_one("First!")

# Callback the function with no argument
print_none()