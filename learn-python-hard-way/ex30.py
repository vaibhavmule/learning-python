# this is exercise 30: Else and If

people = 30 # a variables storing how many people
cars = 40 # a variable storing how many cars
buses = 15 # a variable storing how many buses

# cheking if cars are greater than people
if cars > people:
	print "We should take the cars"

# cheking else if cars are less than people
elif cars < people:
	print "We should not take the cars"

# cheking what else we can do
else:
	print "We can't decide."

# check if buses are greater than cars
if buses > cars:
	print "That's too many buses."

# check else if buses are less than cars
elif buses < cars:
	print "Maybe we could take the buses"

# check what else we can do
else:
	print "We still can't decide."

# check if people are greater than buses
if people > buses:
 	print "Alright, lets just take the buses."

# what else we can do 
else:
	print "Fine, let's stay home then."