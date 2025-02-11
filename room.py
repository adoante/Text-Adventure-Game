class Room:
	def __init__(self, name, description, puzzles):
		self.name = name
		self.description = description
		self.puzzles = puzzles
		self.status = False

	def describe(self):
		print(f"You are in {self.name}.")
		print(f"{self.description}")