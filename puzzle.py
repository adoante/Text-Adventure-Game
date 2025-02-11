# Puzzles are self containted functions that only return False or True

class Puzzle:
	def __init__(self, name, description=None):
		self.name = name
		self.description = description
		self.solved = False
	
	def choose_puzzle(self):
		puzzle = input("> ")
		
	def start_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")
		
		answer = input("> Answer: ").lower()

		if answer == "start":
			self.solved = True
			print("You have solved the puzzle.")
		else:
			print("Incorrect. :(")
		
		return self.solved