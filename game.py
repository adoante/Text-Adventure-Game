from player import Player
from room import Room
from puzzle import *
import sys
from art import *
import time



class Game:
	def __init__(self):
		tprint("Welcome to The Black Phoenix")

		#this is to start the story scroll function
		self.print_story()

		# Puzzles init

		# Start puzzles
		self.security_puzzle = SecurityPuzzle("Security Panel Puzzle", "Solve the math code")
		self.keypad_riddle_puzzle = KeypadRiddlePuzzle("Keypad Riddle Puzzle", "Solve the riddle") 
		self.start_puzzles = (self.security_puzzle, self.keypad_riddle_puzzle)

		# Control Room - Wire cutting and hacking puzzles
		self.wire_puzzle = WireCuttingPuzzle("Wire Cutting Puzzle", "Cut the right wires to disable the lights")
		self.hacking_puzzle = HackingPuzzle("Hacking Puzzle", "Hack into the system to override security")
		self.control_room_puzzles = (self.wire_puzzle, self.hacking_puzzle)

		# Data Center
		self.virus_puzzle = UploadVirusPuzzle("Virus Upload Puzzle", "Upload the virus to the system.")
		self.circuit_puzzle = CircuitMatchingPuzzle("Circuit Matching Puzzle", "Match the nodes to each other.")
		self.data_center_puzzles = (self.virus_puzzle, self.circuit_puzzle)

		# Maintenance Shaft
		self.platform_puzzle = MovingPlatformPuzzle("Moving Platform Puzzle", "Time your jumps to get across.")
		self.deactivation_puzzle = DeactivationPuzzle("Deactivation Puzzle", "Deactivate the electric barriers.")
		self.maintenance_shaft_puzzles = (self.platform_puzzle, self.deactivation_puzzle)

		# Antechamber
		self.Riddle_puzzle = RapidRiddles("Rapid Riddles Puzzle", "Answer all the riddles before the time runs out.")
		self.Song_guesser = guessThatSong("Guess That Song Puzzle", "What well-known song is this string of letters referring to?")
		self.antechamber_puzzles = (self.Riddle_puzzle, self.Song_guesser)

		# Vault
		self.Weight_exchange = weightExchange("Weight Exchange Puzzle","Guess the correct weight of the Black Phoenix so you can switch the diamond out with a counter weight.")
		self.escape_hatch = escapeHatchHack("Escape Hatch puzzle", "Solve the math code to open the escape hatch.")
		self.vault_puzzles = [self.Weight_exchange,self.escape_hatch]

		# Final Room Puzzles
		self.final_lockdown = LockdownOverridePuzzle("Lockdown Override Puzzle", "Hack the final lockdown system to open the last door.")
		self.final_escape = DaringEscapePuzzle("Daring Escape Puzzle", "Distract the guards and slip away with the Black Phoenix.")
		self.final_room_puzzles = (self.final_lockdown, self.final_escape)

		# Rooms init

		self.room_number = 0

		self.rooms = [
			Room(
				"Start",
				"""
				This is where it all begins. 
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
			Room(
				"Control Room",
				"""
				You manage to sneak your way into the Control Room, where the facility's security system is centralized.
				Rows of screens display various surveillance feeds, and a red light flashes urgently above the main panel, signaling a security breach.
				The room feels like a high-tech maze, and you can almost hear the hum of the electronics and the heartbeat of the facility's security
				network.
				It's now or never - if you don't shut down the lights, you'll be caught before you can even get close to the vault
				""",
					self.control_room_puzzles,
					["Decryption Manual", "Security Key"]
			),
			Room(
				"Data Center",
				"""
				You push open a door and step into the Data Center—a vast room with towering servers humming with electricity.
				Rows of blinking lights and whirring fans create a sense of controlled chaos.
				In the center of the room is a terminal connected to the vault's master systems.
				To proceed, you'll need to reroute power and upload a virus to the system.
				You can feel the pressure mounting as a countdown timer on the wall signals how much time you have before reinforcements arrive.
				""",
				self.data_center_puzzles,
				["Big Data", "Circuit Diagram"]
			),
			Room(
				"Maintenance Shaft",
				"""
				The door slams shut behind you, locking you in a dimly lit maintenance shaft.
				You can hear the whirring of mechanical systems and the distant sound of guards mobilizing.
				In front of you is a ventilation panel, partially opened, and beyond it is the only exit.
				The problem? A network of electric barriers and moving platforms blocks your path.
				You'll need to power down the barriers and time your movements to slip through
				""",
				self.maintenance_shaft_puzzles,
				["Floating Platform", "Car Battery"]
			),
			Room(
				"Antechamber",
				"""
				You burst into the Vault Antechamber—the final barrier before the prize. 
				In front of you stands a massive, reinforced door covered in intricate locking mechanisms and glowing symbols.
				A countdown timer blinks ominously above the door, triggered by the facility's breach detection.
				The locking system is designed to be solved through a series of riddles and combinations, each more complex than the last.
				The air is thick with tension, and every second counts as distant footsteps and alarms echo through the halls.
				Solve the puzzles in time, or risk being permanently sealed inside with the vault forever out of reach.
				""",
				self.antechamber_puzzles,
				["Rail Gun", "Meteorite"]
			),
			Room(
				"Vault",
				"""
				The vault door hisses open, revealing a pedestal in the center of a stark, brightly lit room.
				Sitting on the pedestal is the Black Phoenix—the diamond that's driven you to plan this heist for months.
				It sparkles with an otherworldly brilliance under the harsh lights.
				But as you step forward, an alarm blares. The facility has entered full lockdown.
				There's no time to think. You must escape with the prize—now.
				""",
				self.vault_puzzles,
				["Black Phoenix", "Black Phoenix: Electric Boogaloo"]
				
			),
			Room(
                "Final Extraction",
                """
                Sirens are blaring and red lights flash across the corridor.
                This is your last obstacle before disappearing into the night with the Black Phoenix.
                A heavy blast door stands in your way, sealed by the facility's final lockdown override.
                Guards are stationed at every exit. This is the do-or-die moment: 
                solve these final challenges to break the lockdown and make a daring escape!
                """,
                self.final_room_puzzles,
                ["Smoke Bomb", "Guard Uniform"]
            )
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

	# Game ending screen
	def end_screen(self):
		story = """
		As the final barrier gives way, you sprint into the night, the Black Phoenix secured in your grip.
		The city's skyline stretches before you, neon lights flickering against the rain-soaked streets.
		Behind you, alarms wail and distant shouts echo through the facility, but it's too late—they'll never catch you now.
		Vanishing into the shadows, you slip into the carefully planned escape route, leaving nothing behind but mystery and legend.
		The heist of the century is complete, and the world will wake to the news of the impossible.
		
		You are more than just a thief—you are a ghost, a myth, a legend."
		"""

		#splitting the story into lines and print each line with a small delay for a scrolling effect
		for line in story.splitlines():
			print(line)
			time.sleep(1) #this will adjust this for longer/shorter pauses between lines

		# score based on items and the number of characters in that string
		score = sum(len(i) for i in self.player.items)

		print("\nYou have escaped with:\n")
		print(f"{', '.join(self.player.items)}")
		print(f"Score: {score}")
		
		tprint("The End!")

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
					self.end_screen()
					sys.exit()
				# Move player to next room
				else:
					self.player.current_room = self.rooms[self.room_number]

if __name__ == "__main__":
	game = Game()
	game.start_game()
