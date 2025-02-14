from player import Player
from room import Room
from puzzle import *
import sys
from art import *
import time
#from puzzle import SecurityPuzzle, KeypadRiddlePuzzle, WireCuttingPuzzle, HackingPuzzle
#from puzzle import WireCuttingPuzzle


class Game:
	def __init__(self):
		tprint("Welcome to The Black Phoenix")

		#this is to start the story scroll function
		self.print_story()

		# Puzzles init
		#print(self.security_panel_puzzle)
		#print(KeypadRiddlePuzzle)


		# Start puzzles
		
		self.security_puzzle = SecurityPuzzle("Security Panel Puzzle", "Solve the math code")
		self.keypad_riddle_puzzle = KeypadRiddlePuzzle("Keypad Riddle Puzzle", "Solve the riddle") 
		print(self.security_puzzle)
		self.start_puzzles = (self.security_puzzle, self.keypad_riddle_puzzle)
		#self.start_puzzle1 = StartPuzzle("StartPuzzle1", "This is the start puzzle 1")
		#self.start_puzzle2 = StartPuzzle("StartPuzzle2", "This is the start puzzle 2")
		#self.start_puzzles = (self.start_puzzle1, self.start_puzzle2)

		

		"""self.timer_puzzle1 = TimerPuzzle("Timer puzzle 1", "This is a timer puzzle")
		self.timer_puzzle2 = TimerPuzzle("Timer puzzle 2", "This is a timer puzzle")
		self.timer_puzzles = (self.timer_puzzle1, self.timer_puzzle2)"""

		"""self.control_room_puzzles = [
			WireCuttingPuzzle("Disarm the lights", "Disarm the lights by cutting the wires in the correct order"),
			HackingPuzzle("Hack the Mainframe", "Guess the password to gain control of the security systems")
		]"""
		# Wire cutting and hacking puzzles
		self.wire_puzzle = WireCuttingPuzzle("Wire Cutting Puzzle", "Cut the right wires to disable the lights")
		self.hacking_puzzle = HackingPuzzle("Hacking Puzzle", "Hack into the system to override security")
		print(self.wire_puzzle)
		self.timer_puzzles = (self.wire_puzzle, self.hacking_puzzle)


		# Rooms init
		self.room_number = 0

		self.rooms = [

			Room(
				"Start",
				"""This is where it all begins. 
			You find yourself crouched in a shadowy corner of the alley outside the facility,
			reviewing the map of the building one last time. The rain beats down,
			muffling the sounds of distant footsteps. You've been planning this heist for months, gathering every scrap of 
			intelligence and analyzing every possible escape route. You know this building better than its own security team - every
			bypassed camera, every hidden vent, It's your playground now.
				

			As you enter the facility through a vent you disabled weeks ago, the dim emergency lights flicker, casting eerie shadows
			across the metal walls. You're not just breaking in-you're walking a path you've already rehearsed in you mind a thousand times.
				
				
			Despite the overwhelming confidence in your plan, you know better than to let your guard down. Your first challenge awaits. Solve
			these simple security measures to proceed further. There's no turning back now.
			""",
				self.start_puzzles,
				["Pass Key", "Camera App"]
			),
			#Room("Start", "This is the Start Screen", self.start_puzzles, ["item1", "item2"]),
			#Room("Timer", "This is the Timer puzzle room", self.timer_puzzles,  ["item3", "item4"]),
			Room(
				"Control Room",
				"""You manage to sneak your way into the Contrl Room, where the facility's security system is centralized.
				Rows of screens display various surveillance feeds, and a red light flashes urgently above the main panel, signaling a security breach.
				The room feels like a high-tech maze, and you can almost hear the hum of the electronics and the heartbeat of the facility's security
				network.
				It's now or never - if you don't shut down the lights, you'll be caught before you can even get close to the vault
				""",
					self.timer_puzzles,
					["Decryption Manuel", "Security Key"]
			),

			#Room("Timer", "This is the Timer puzzle room", self.timer_puzzles, ["Disguise Kit", "Decryption Manul"]),
			]
			

		
		# Player init
		self.player = Player()
		self.player.current_room = self.rooms[self.room_number]

	def print_story(self):
		#func to print the story with a scrolling effect
		story = """
		Welcome to The Black Phoenix Heist
		
		You are a legendary diamond thief, renowned for your ability to infiltrate the most secure locations.
		Tonight, you're taking on your biggest challenge yet - stealing the Black Phoenix, the most coveted
		and dangerous diamond in the world. Hidden deep within a secret government facility, guarded by intricate puzzles, 
		laser grids, and security teams, this is the job of a lifetime.
		
		Will you be able to escape with the prize, or will the authorities catch you before you can make your
		daring escape?
		
		Get ready for the heist of the century...
		"""
		#splitting the story into lines and print each line with a small delay for a scrolling effect
		for line in story.splitlines():
			print(line)
			time.sleep(1) #this will adjust this for longer/shorter pauses between lines
		print("\nType 'Next' to begin your journey or 'Exit' to quit the game.")

		#this is for waiting for the players input so the game can start
		while True:
			command = input("> ").lower()
			if command == "next":
				print("Starting the heist...")
				break
			elif command == "exit":
				print("Exiting the game. Goodbye!")
				sys.exit()
			else:
				print("Invalid command. Type 'Next' to begin or 'Exit' to quit.")		

	def start_game(self):
		self.player.print_commands()
		print()

		# Describe the room and new rooms once to the player 
		describe_flag = True

		while True:
			
			if describe_flag:
				self.player.current_room.describe()
				describe_flag = False

			# Get player input
			self.player.input_command()
			
			# Move player to new room
			if self.player.current_room.status:
				# Update room number
				self.room_number += 1

				# New room update describe_flag
				describe_flag = True

				# Determine if player has beat the game
				if self.room_number == len(self.rooms):
					print("You beat the game!")
					sys.exit()
				# Move player to next room
				else:
					self.player.current_room = self.rooms[self.room_number]

if __name__ == "__main__":
	game = Game()
	game.start_game()
