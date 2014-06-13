# This is Exercise 8 : Printing, Printing

# A variable storing formatting
formatter = "%r %r %r %r"

# Print a variable and includes numbers 1, 2, 3, 4
print formatter % (1, 2, 3, 4)

# Print a variable and includes strings "one, two, three, four"
print formatter % ("one", "two", "three", "four")

# Print a variable and includes booleans (True, False, False, True)
print formatter % (True, False, False, True)

# Print a variable and includes variable as formatter
print formatter % (formatter, formatter, formatter, formatter)

# Print a variable with formatter and includes four sentence using comma
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
) 