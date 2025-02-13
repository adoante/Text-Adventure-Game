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

					if len(self.current_room.items) == 0:
						print("There are no items in this room to pick")
						break

					#listing available items
					for i, item in enumerate(self.current_room.items, 1):
						print(f"{i}: {item}")
					
					item = input("\n> ").lower()

					try:
						item_index = int(item) - 1
						if 0 <= item_index < len(self.current_room.items):
							item_to_take = self.current_room.items.pop(item_index)
							self.items.append(item_to_take)
							print(f"You took the {item_to_take}")
							break
						else:
							print("Not an option.\n")
							break
						
					except:
						print("Not an option\n")
						continue

			else:
				print("You must solve both puzzles to move on")

		elif command == "status":
				for puzzle in self.current_room.puzzles:
					print(f"{puzzle.name}: {'Solved' if puzzle.solved else 'Unsolved'}")

		#print items that in players inventory
		elif command == "items":
				if self.items:
					print(f"Items in your inventory: {', '.join(self.items)}")
				else:
					print("You have no items in your inventory")

		#prints available commands
		elif command == "cmd":
			self.print_commands()