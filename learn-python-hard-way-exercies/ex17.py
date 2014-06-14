# This is Exercise 17: More Files

# Import argv module from sys package
from sys import argv

# Import exists module from os.path packege
from os.path import exists

# Asking for arguments to copying file
script, from_file, to_file = argv

# Showing which file copying into another file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one lines too, how?
# open the file
in_file = open(from_file)

# read the file
indata = in_file.read()

# a sentence showing file size
print "The input file is %d bytes long" % len(indata)

# check if file exists or not
print "Does the output file exists? %r" % exists(to_file)

# asking for permission to copying file
print "Ready, hit RETURN to continue, CTRL-C to abort."

# asking input to confirm permission
raw_input()

# open file to write
out_file = open(to_file, "w")

# write the file
out_file.write(indata)

# tell, it's done
print "Alright, all done"

# close the file which is copied the data 
out_file.close

# close the file which is data copied from
in_file.close