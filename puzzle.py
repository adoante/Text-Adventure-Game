from abc import ABC, abstractmethod

class Puzzle(ABC):
	def __init__(self, name, description=None):
		self.name = name
		self.description = description
		self.solved = False
	
	@abstractmethod
	def run_puzzle(self):
		pass
	
class StartPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")
		
		answer = input("> Answer: ").lower()

		if answer == "start":
			self.solved = True
			print("You have solved the puzzle.")
		else:
			print("Incorrect. :(")
		
		return self.solved