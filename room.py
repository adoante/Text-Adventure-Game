import textwrap


class Room:
	def __init__(self, name, description, puzzles, items):
		self.name = name
		self.description = description
		self.puzzles = puzzles
		self.status = False
		self.items = items

	def describe(self):
		print(f"You are in {self.name}.")
		print(f"{self.description}.")

	def remove_item(self, item):
		if item in self.items:
			self.items.remove(item)
			print(f"{item} has been removed from the room.")
		else:
			print(f"{item} is not in the room")
	