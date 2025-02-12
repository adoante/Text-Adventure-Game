from player import Player
from room import Room
from puzzle import *
import sys
from art import *

class Game:
	def __init__(self):
		tprint("Welcome to [title]")

		# Puzzles init

		# Start puzzles 
		self.start_puzzle1 = StartPuzzle("Start puzzle 1", "This is the start puzzle 1")
		self.start_puzzle2 = StartPuzzle("Start puzzle 2", "This is the start puzzle 2")
		self.start_puzzles = (self.start_puzzle1, self.start_puzzle2)

		self.timer_puzzle1 = TimerPuzzle("Timer puzzle 1", "This is a timer puzzle")
		self.timer_puzzle2 = TimerPuzzle("Timer puzzle 2", "This is a timer puzzle")
		self.timer_puzzles = (self.timer_puzzle1, self.timer_puzzle2)

		# Rooms init
		self.room_number = 1

		self.rooms = [
			Room("Start", "This is the Start Screen", self.start_puzzles),
			Room("Timer", "This is the Timer puzzle room", self.timer_puzzles),
			]
		
		# Player init
		self.player = Player()
		self.player.current_room = self.rooms[self.room_number]

	def start_game(self):
		self.player.print_commands()
		print()

		describe_flag = True

		while True:
			
			if describe_flag:
				self.player.current_room.describe()
				describe_flag = False

			self.player.input_command()

			if self.player.current_room.status:
				self.room_number += 1
				describe_flag = True
				if self.room_number == len(self.rooms):
					print("You beat the game!")
					sys.exit()
				else:
					self.player.current_room = self.rooms[self.room_number]
				