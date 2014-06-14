# This is Exercise 14: Prompting and Passing

# Import sys modules and argv is an argument variable
# which holds arguments that you pass on Pyhton script
from sys import argv

# Unpacking and asign value to variables
script, user_name = argv

# Prompt 
prompt = '> '

# Print a sentence
print "Hi %s, I'm the %s script." % (user_name, script)

# Print a sentence
print "I'd like to you ask you a questions."

# Print a sentence
print "Do you like me %s?" % user_name

# prompt
likes = raw_input(prompt)

# Prinitng and asking question as prompt
print "Where do you live %s?" % user_name

# Prompt 
lives = raw_input(prompt)

# Prinitng and asking about computer
print "What kind of computer do you have?"

# Prompt
computer = raw_input(prompt)

# printing sentences and printing varibale using %r
print """
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)