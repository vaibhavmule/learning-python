# this is exercise 33: while loop

i = 0 # a variable storing "0"
numbers = [] # a variable storing empty arrays

# while runt till 6
while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1 
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num