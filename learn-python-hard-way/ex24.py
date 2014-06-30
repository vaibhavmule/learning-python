# this is exercise 23: More Practice

# print a sentence
print "Let's practice everything."

# print a sentence with backslash
print 'You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.'

# a variable storing poem
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explanation
\n\t\twhere there is none.
"""

# print the poem
print "-------------"
print poem
print "-------------"

# a variable storing mathematical expression
five = 10 - 2 + 3 - 6

# print the answer within sentence with formatter
print "This shoulb be five: %s" % five

# define the function 
def secret_formula(started):

# creating argument multyply by 500
	jelly_beans = started * 500

# check the jars
	jars = jelly_beans / 1000

# check the crates
	crates = jars / 100

# return the value
	return jelly_beans, jars, crates

# a variable storing integer
start_point = 10000

# callback of function
beans, jars, crates = secret_formula(start_point)

# print the sentence
print "With a starting point of: %d" % start_point

# print answer
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# again mathematical expression in a variable
start_point = start_point / 10

# print the sentence
print "We can also do that this way:"

# print the answers
print "We'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)