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