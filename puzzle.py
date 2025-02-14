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
# Uses threading for the countdown timer because input() haults the program
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

		answer = input()

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
		#pass
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
				print("Acces granted! You have succesfully hacked into the system")
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