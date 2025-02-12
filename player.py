import sys

class Player:
	def __init__(self):
		self.current_room = None

	def print_commands(self):
		print("Commands: ")
		print("--- Exit  : Exit the game.")
		print("--- Desc  : Room Description.")
		print("--- Solve : Pick a puzzle to solve.")
		print("--- Next  : Move to next room.")
		print("--- Status: Status of puzzles.")
		print("--- CMD   : Print commands.")

	def input_command(self):
		command = input("\n> ").lower()
		self.process_command(command)
	
	def process_command(self, command):
		if command == "exit":
			print("Exiting game.")
			sys.exit()

		elif command == "desc":
			self.current_room.describe()

		elif command == "solve":
			puzzle1 = self.current_room.puzzles[0]
			puzzle2 = self.current_room.puzzles[1]

			print(f"1: {puzzle1.name}")
			print(f"2: {puzzle2.name}")

			puzzle_pick = input("\n> ").lower()

			if int(puzzle_pick) == 1:
				puzzle1.run_puzzle()
			elif int(puzzle_pick) == 2:
				puzzle2.run_puzzle()	
						

		elif command == "next":
			puzzle1 = self.current_room.puzzles[0].solved
			puzzle2 = self.current_room.puzzles[1].solved

			if puzzle1 and puzzle2:
				self.current_room.status = True
			else:
				print("You must solve both puzzles to move on.")

		elif command == "status":
			puzzle1 = self.current_room.puzzles[0]
			puzzle2 = self.current_room.puzzles[1]

			for puzzle in self.current_room.puzzles:
				if (puzzle.solved):
					print(f"{puzzle.name}: Solved")
				else:
					print(f"{puzzle.name}: Unsolved")

		elif command == "cmd":
			self.print_commands()
