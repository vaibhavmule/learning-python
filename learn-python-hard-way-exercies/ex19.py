# this is exercise 19: Functions and Variables

# a function that ask for cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):

# print how many cheese you have
	print "You have %d cheeses!" % cheese_count

# print how many boxes of crackers
	print "You have %d boxes of crackers" % boxes_of_crackers

# print that's enough for a party
	print "Man that's enough for a party"

# print a sentence with \n
	print "Get a blanket.\n"

# print a sentence saying to callback
print "We can just give the function numbers directly:"

# callback the function
cheese_and_crackers(20, 30)

# print a sentence saying to do with variables
print "OR, we can use varaibles form our script:"

# a variable storing a argument
amount_of_cheese = 10

# a variable storing second argument
amount_of_crackers = 50

# call the funtion with two varibles as argument
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print a sentence 
print "We can even do math inside too:"

# call the functions with math expression
cheese_and_crackers(10 + 20, 5 + 6)

# print a sentence 
print "And we can combine the two, variables and math:"

# call the funciton with math expressions
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 
