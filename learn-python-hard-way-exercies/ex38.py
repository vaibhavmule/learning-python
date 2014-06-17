# this is exercise 38: doing things to list

# a varibale storing list of things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print saying there is not tne things
print "Wait there's not 10 htings in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girls", "Boys"]

while len(stuff) !=10:
	next_one = more_stuff.pop()
	print "Adding", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
print "There we go: ", stuff
print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar
