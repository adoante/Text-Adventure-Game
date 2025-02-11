import sys

class Player:
	def __init__(self, name):
		self.name = name
		self.current_room = None

	def input_command(self):
		command = input("> ").lower()
		self.process_command(command)
	
	def process_command(self, command):
		if command == "exit":
			print("Exiting game.")
			sys.exit()

		elif command == "describe":
			self.current_room.describe()

		elif command == "1":
			self.current_room.puzzles[0].start_puzzle()

		elif command == "2":
			self.current_room.puzzles[1].start_puzzle()

		elif command == "next":
			puzzle1 = self.current_room.puzzles[0].solved
			puzzle2 = self.current_room.puzzles[1].solved

			if puzzle1 and puzzle2:
				self.current_room.status = True
			else:
				print("You must solve both puzzles to move on.")
