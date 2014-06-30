from sys import exit

class Room(object):

	def enter(self):
		print "Hi, Welcome Sherlock"
		exit(1)

class BedRoom(Room):

	def enter(self):
		print "Hi this is bedroom"

class Garden(Room):

	def enter(self):
		print "HI this is garden"

class office(Room):

	def enter(self):
		print "hi this is office"

class SportRoom(Room):

	def enter(self):
		print "hi this is Sportroom"

		return 'mission_complete'