from player import Player
from room import Room
from puzzle import Puzzle

# Puzzles init
start_puzzle1 = Puzzle("start puzzle 1", "This is the start puzzle 1")
start_puzzle2 = Puzzle("start puzzle 2", "This is the start puzzle 2")

# Rooms init
room_number = 0

rooms = [
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2]),
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2]),
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2]),
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2]),
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2]),
	Room("start", "This is the Start Screen.", [start_puzzle1, start_puzzle2])
	]

# Player init
player = Player("test_player")
player.current_room = rooms[room_number]

# Game loop

print("Welcome to [title]")
print("Commands: ")
print("--- Exit : Exit the game.")
print("--- Desc : Room Description.")
print("--- 1    : Solve puzzle 1.")
print("--- 2    : Solve puzzle 2.")

while True:
	player.input_command()

	if player.current_room.status:
		room_number += 1
		player.current_room = rooms[room_number]
	

