# This is Exercise 4 : Variables and Names

# cars given value of 100
cars = 100

# assigning 4.0 value to space_in_a_car variable
space_in_a_car = 4

# There are 30 drivers
drivers = 30

# There are 90 Passengers
passengers = 90

# Calculate how many cars are not driven by subtracting "drivers" from "cars".
cars_not_driven = cars - drivers

# Creating new variable and assigning value of drivers.
cars_driven = drivers

# Calculate car capacity by multiplying cars driven into space in car.
carpool_capacity = cars_driven * space_in_a_car

# Calculate Average passengers by dividing passengers to cars driven.
average_passengers_per_car = passengers / cars_driven

# Print the cars which are avalable with sentence.
print "There are", cars, "cars avalable."

# Print how many drivers are there with sentence.
print "There are only", drivers, "drivers available."

# Print how many cars are empty today with sentence.
print "There will be", cars_not_driven, "empty cars today."

# Print carpool capacity with sentence.
print "We can transport", carpool_capacity, "people today."

# Print how many passengers to carpool today with sentence.
print "We have", passengers, "to carpool today."

# Print average passenger per car with sentence.
print "We need to put about", average_passengers_per_car, "in each car."