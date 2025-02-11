from player import Player
from room import Room
from puzzle import Puzzle
import sys

class Game:
	def __init__(self):
		print("Welcome to [title]\n")

		# Puzzles init

		# Start puzzles 
		self.start_puzzle1 = Puzzle("Start puzzle 1", "This is the start puzzle 1")
		self.start_puzzle2 = Puzzle("Start puzzle 2", "This is the start puzzle 2")
		self.start_puzzles = (self.start_puzzle1, self.start_puzzle2)

		# Rooms init
		self.room_number = 0

		self.rooms = [
			Room("Start", "This is the Start Screen.", self.start_puzzles)
			]
		
		# Player init
		self.player = Player()
		self.player.current_room = self.rooms[self.room_number]

	def start_game(self):
		self.player.print_commands()

		while True:
			self.player.input_command()

			if self.player.current_room.status:
				self.room_number += 1

				if self.room_number == len(self.rooms):
					print("You beat the game!")
					sys.exit()
				else:
					self.player.current_room = self.rooms[self.room_number]
				