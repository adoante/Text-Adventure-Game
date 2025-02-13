import sys

class Player:
	def __init__(self):
		self.current_room = None
		self.items = []

	# prints commands
	def print_commands(self):
		print("Commands: ")
		print("--- Exit  : Exit the game.")
		print("--- Desc  : Room Description.")
		print("--- Solve : Pick a puzzle to solve.")
		print("--- Next  : Move to next room.")
		print("--- Status: Status of puzzles.")
		print("--- Items : Display Items.")
		print("--- CMD   : Print commands.")

	# Asks player for input command
	def input_command(self):
		command = input("\n> ").lower()
		self.process_command(command)
	
	# Process all player input commands
	def process_command(self, command):
		# Exits the entire game
		if command == "exit":
			print("Exiting game.")
			sys.exit()

		# Describes the room the player is in
		elif command == "desc":
			self.current_room.describe()

		# Ask you to pick a puzzle to solve
		elif command == "solve":
			puzzle1 = self.current_room.puzzles[0]
			puzzle2 = self.current_room.puzzles[1]

			print(f"1: {puzzle1.name}")
			print(f"2: {puzzle2.name}")

			puzzle_pick = input("\n> ").lower()

			# Player input needs to be 1 or 2
			try:
				if int(puzzle_pick) == 1:
					puzzle1.run_puzzle()
				elif int(puzzle_pick) == 2:
					puzzle2.run_puzzle()
				else:
					print("Not an option.")
			except:
				print("Not an option.")			

		# Moves player to next room if both puzzles are solved
		# Asks player to pick an item to take from current room
		elif command == "next":
			puzzle1 = self.current_room.puzzles[0].solved
			puzzle2 = self.current_room.puzzles[1].solved

			if puzzle1 and puzzle2:
				self.current_room.status = True

				# Player input needs to be 1 or 2
				# Must take an item before moving
				while True:
					print("You solved both puzzles.")
					print("Pick an item to take with you.\n")

					item1 = self.current_room.items[0]
					item2 = self.current_room.items[1]

					print(f"1: {item1}")
					print(f"2: {item2}")
				
					item = input("\n> ").lower()

					try:
						if int(item) == 1:
							self.items.append(item1)
							break
						elif int(item) == 2:
							self.items.append(item2)
							break
						print("Not an option.\n")
					except:
						print("Not an option.\n")
						continue
			else:
				print("You must solve both puzzles to move on.")

		# Print status of puzzles
		elif command == "status":
			puzzle1 = self.current_room.puzzles[0]
			puzzle2 = self.current_room.puzzles[1]

			for puzzle in self.current_room.puzzles:
				if (puzzle.solved):
					print(f"{puzzle.name}: Solved")
				else:
					print(f"{puzzle.name}: Unsolved")

		# Print items
		elif command == "items":
			print(f"Items: {self.items}")

		# Print Commands 
		elif command == "cmd":
			self.print_commands()
