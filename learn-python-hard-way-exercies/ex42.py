# this is exercise 42: is-a, has-a. Objects, and Classes
# Animal is-a object (yes, sort of confusing) look at the extra credit

class Animal(object):
	pass

## Dog is a class
class Dog(Animal):

	def __init__(self, name):
		## Dog has a name
		self.name = name

## Cat is a class
class Cat(Animal):

	def __init__(self, name):
		## Cat has a name
		self.name = name

## Person is object
class Person(object):

	def __init__(self, name):
		## Person has a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is object 
class Employee(Person):

	def __init__(self, name, salary):
		## Emplpoyee has a name
		super(Employee, self).__init__(name)
		## Emplpoyee has a salary
		self.salary = salary

## Fish is object 
class Fish(object):
	pass

## Salmon is object 
class Salmon(Fish):
	pass

## Halibut is object 
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is a cat 
satan = Cat("Satan")

## Mary is a person
mary = Person("Mary")

## mary has a pet named satan
mary.pet = satan

## frank has salary 120000
frank = Employee("Frank", 120000)

## frank has pet named rover
frank.pet = rover

## flipper is a fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is Halibut means a fish
harry = Halibut()
