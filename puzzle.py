class Puzzle:
	def __init__(self, name, description=None):
		self.name = name
		self.description = description
		self.solved = False
		
	def choose_puzzle(self, name):
		if name == "Start puzzle 1":
			self.start_puzzle()
		elif name == "Start puzzle 2":
			self.start_puzzle()

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