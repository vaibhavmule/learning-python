# Exercise 45: You Make Your Game

from engine import Engine
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

class Office(Room):

	def enter(self):
		print "hi this is office"

class SportRoom(Room):

	def enter(self):
		print "hi this is Sportroom"

		return 'mission_complete'

class Map(object):

	rooms = {
		'bed_room' : BedRoom(),
		'garden': Garden(),
		'office': Office(),
		'SportRoom': SportRoom()
	}

	def __init__(self, start_room):
		self.start_room = start_room
		print "start room", self.start_room

	def next_room(self, room_name):
		print "start room in next"
		val = Map.room.get(room_name)
		print "next room return", val

	def open_room(self):
		return self.next_room(self.start_room)

a_map = Map('SportRoom')
a_game = Engine(a_map)
a_game.play
