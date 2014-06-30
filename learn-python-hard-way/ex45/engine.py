class Engine(object):

	def __init__(self, room_map):
		print "engine has room_map", room_map
		self.room_map = room_map

	def play(self):
		current_room = self.room_map.open_room()
		print "Go first room", current_room

		while True:
			print "n------------"
			next_room_name = current_room.enter()
			print "nect room", next_room_name
			current_room = self.room_map.next_room(next_room_name)
			print "map return new room", current_room