from abc import ABC, abstractmethod

import sys

import time
import threading

# Puzzle Interface
# Must implement run_puzzle() and return self.solved
class Puzzle(ABC):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.solved = False

	@abstractmethod
	def run_puzzle(self):
		pass
	
# Example Puzzle
class StartPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")
		
		answer = input("\n> Answer: ").lower()

		if answer == "exit":
			sys.exit()

		elif answer == "start":
			self.solved = True
			print("You have solved the puzzle.")
		
		else:
			print("Incorrect. :(")
		
		return self.solved

# Example Timer Puzzle
# Uses threading for the countdown timer because input() halts the program
class TimerPuzzle(Puzzle):
	
	# Example function that threading requires to be passed into it
	def timer_time(self, stop):
		countdown_time = 10

		while countdown_time:
			if stop():
				break

			mins, secs = divmod(countdown_time, 60) 
			timer = '{:02d}:{:02d}'.format(mins, secs)
			
			timer_answer = ((f"\n{timer}> Answer: ").lower())

			print(timer_answer, end="")
			
			time.sleep(2)
			countdown_time -= 1

			if countdown_time == 0:
				print("\nTime's up! Try again.")

	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		# Basic threading setup
		stop_thread = False
		threading1 = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
		threading1.daemon = True
		threading1.start()

		answer = input().lower()

		if answer == "exit":
			sys.exit()

		elif answer == "timer":
			self.solved = True
			print("You have solved the puzzle.")
			
		else:
			print("Incorrect. :(")
		
		# Remember to stop and join the thread
		stop_thread = True
		threading1.join()
		
		return self.solved
	
class KeypadRiddlePuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		answer = input("The keypad asks: 'I am taken from a mine and shut up in a wooden case, but used by almost every person. What am I?' ").lower()
		if answer == "pencil":
			self.solved = True
			print("Correct! The riddle puzzle is solved")
		else:
			print("Incorrect. Try again.")
		return self.solved
		
class SecurityPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		answer = input("The screen flashes '3 + 5'. Enter the correct code: ").lower()
		if answer == "8":
			self.solved = True
			print("Correct! The door unlocks.")
		else:
			print("Incorrect. Try again.")
		return self.solved
	
# Hacking puzzle
class HackingPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		print("You must guess the correct password within 3 attempts")

		correct_password = "phoenix"
		attempts = 3

		for attempt in range(1, attempts + 1):
			guess = input(f"Attempt {attempt}/{attempts} - Enter password: ").lower()

			if guess == correct_password:
				self.solved = True
				print("Access granted! You have successfully hacked into the system")
				break
			else:
				print("Access denied. Try again.")
		if not self.solved:
			print("Too many failed attempts. The system locks you out.")

		return self.solved
	
# wire cutting puzzle
class WireCuttingPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		print("The lights are flickering, you need to cut the right wires to disarm the security system")
		print("There are 3 wires: red, blue, yellow")
		
		# hardcoded correct sequence (for now)
		correct_sequence = ["red", "yellow", "blue"]
		sequence = []

		for i in range(3):
			wire = input(f"Cut wire {i + 1}:").lower()
			sequence.append(wire)

		if sequence == correct_sequence:
			self.solved = True
			print("You successfully cut the wires in the right order! The lights go out")
		else:
			print("Incorrect wire cutting sequence. The lights remain on, security may be on the way")
		return self.solved
	
# Upload a virus puzzle
class UploadVirusPuzzle(Puzzle):

	input_time = 0

	def timer_time(self, stop):
		global input_time
		countdown_time = 0

		while True:
			if stop():
				break

			mins, secs = divmod(countdown_time, 60) 
			timer = '{:02d}:{:02d}'.format(mins, secs)
			
			timer_answer = ((f"\n{timer}> Answer: ").lower())

			print(timer_answer, end="")
			
			time.sleep(1)
			countdown_time += 1
			input_time = countdown_time

	def run_puzzle(self):
		global input_time

		print(f"{self.name}")
		print(f"{self.description}")

		print("You must input the virus code at the specified time to successfully infect the system.")

		#virus_code = ['abc', 'de', 'fgh', 'ijk', 'lmno', 'p']
		virus_code = ['a', 'd', 'f', 'i', 'l', 'p']
		virus_code_count = 0
		timing = [1, 3, 4, 2, 3, 4]

		for virus in enumerate(virus_code):
			print(f"You must enter '{virus[1]}' at '{timing[virus[0]]}' seconds.")
			time.sleep(1.5)

			# threading setup
			stop_thread = False
			threading1 = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
			threading1.daemon = True
			threading1.start()

			answer = input().lower()

			index = virus[0]
			
			if answer != virus[1] and input_time != timing[index]:
				print("Error! Virus upload failed! Wrong code and timing! ❌")
				break
			elif answer != virus[1]:
				print("Error! Virus upload failed! Wrong code! ❌")
				break
			elif input_time != timing[index]:
				print("Error! Virus upload failed! Wrong timing! ❌")
				break
			elif answer == virus[1] and input_time == timing[index]:
				print("Successful input! ✔️")
				virus_code_count += 1

			stop_thread = True
			threading1.join()
			input_time = 0
		
		# Check if all inputs where correct
		if virus_code_count == len(virus_code):
			self.solved = True
			print(" ⌨️ Virus upload successful! ⌨️")

		# Remember to stop and join the thread
		stop_thread = True
		threading1.join()
		
		return self.solved
	
class CircuitMatchingPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		print("You must match the circuit nodes to each other.")
		print("The nodes are labeled with numbers perhaps there's a pattern to it.")

		nodes_key = [(2, 11), (13, 29), (31, 47), (53, 71), (73, 97)]

		nodes = [
			2, 3, 5, 7, 11,
			13, 17, 19, 23, 29,
			31, 37, 41, 43, 47,
			53, 59, 61, 67, 71,
			73, 79, 83, 89, 97
		   ]

		print("Nodes: ")	
		print(f"| {nodes[0]}  | {nodes[1]}  | {nodes[2]}  | {nodes[3]}  | {nodes[4]}")
		print(f"| {nodes[5]} | {nodes[6]} | {nodes[7]} | {nodes[8]} | {nodes[9]}")
		print(f"| {nodes[10]} | {nodes[11]} | {nodes[12]} | {nodes[13]} | {nodes[14]}")
		print(f"| {nodes[15]} | {nodes[16]} | {nodes[17]} | {nodes[18]} | {nodes[19]}")
		print(f"| {nodes[20]} | {nodes[21]} | {nodes[22]} | {nodes[23]} | {nodes[24]}")

		for nodes in nodes_key:
			answer = input(f"> Node {nodes[0]} -> ").lower()

			try:
				answer = int(answer)
			except:
				print("Bad input! ❌")
				self.solved = False
				return self.solved
			
			if int(answer) != nodes[1]:
				print("Bad connection made! ❌")
				self.solved = False
				break
			else:
				print("Good connection! ✔️")
				self.solved = True

		if (self.solved):
			print("⚡Power successfully rerouted! ⚡")
		return self.solved

# Maintenance Shaft Puzzles

class MovingPlatformPuzzle(Puzzle):
	def run_puzzle(self):
		return super().run_puzzle()
	
class DeactivationPuzzle(Puzzle):
	def run_puzzle(self):
		return super().run_puzzle()
