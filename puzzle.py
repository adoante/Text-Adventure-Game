from abc import ABC, abstractmethod

import sys

import time
import threading

import random 

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

		attempts = 0
		hint_given = False  # To track if a hint has already been given
		correct_answer = "footsteps"
		answer = None

		while attempts < 3:
			answer = input("The more you take, the more you leave behind. What am I? - ").lower()
			if answer == "exit":
				sys.exit()

			if answer == correct_answer:
				self.solved = True
				print("Correct! The riddle puzzle is solved")
				break
			else:
				attempts += 1
				print("Incorrect. Try again.")
				if attempts == 1 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: It is something that happens when you walk")
						hint_given = True
				elif attempts == 2 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: It's a clue related to walking and movement")
						hint_given = True
		return self.solved
		
		
class SecurityPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")


		attempts = 0
		hint_given = False  # To track if a hint has already been given
		answer = None

		while attempts < 3:
			answer = input("The screen flashes '3 + 5'. Enter the correct code: ").lower()
			if answer == "exit":
				sys.exit()

			if answer == "8":
				self.solved = True
				print("Correct! The door unlocks.")
				break
			else:
				attempts += 1
				print("Incorrect. Try again.")
				if attempts == 2 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: You have five apples then you add 3 to it. What do you get?")
						hint_given = True
				elif attempts == 3:
					print("You've failed to solve it. The system locks you out.")

		"""answer = input("The screen flashes '3 + 5'. Enter the correct code: ").lower()
		if answer == "8":
			self.solved = True
			print("Correct! The door unlocks.")
		else:
			print("Incorrect. Try again.")"""
		
		return self.solved
	
# Hacking puzzle
class HackingPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		print("You must guess the correct password within 3 attempts")

		correct_password = "phoenix"
		attempts = 3
		hint_given = False  # Track if a hint has been given

		for attempt in range(1, attempts + 1):
			guess = input(f"Attempt {attempt}/{attempts} - Enter password: ").lower()

			if guess == correct_password:
				self.solved = True
				print("Access granted! You have successfully hacked into the system")
				break
			else:
				print("Access denied. Try again.")
				if attempt == 2 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: It's the name of a mythical bird (Dumbledore's pet)")
						hint_given = True
		if not self.solved:
			print("Too many failed attempts. The system locks you out.")


		"""correct_password = "phoenix"
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
			print("Too many failed attempts. The system locks you out.")"""

		return self.solved
	
# wire cutting puzzle
class WireCuttingPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		attempts = 0
		hint_given = False  # Tracks if a hint has been given
		
		while attempts < 3:
			print("\nThere are 3 wires: red, blue, yellow")
			wire1 = input("Cut wire 1: ").lower()
			wire2 = input("Cut wire 2: ").lower()
			wire3 = input("Cut wire 3: ").lower()

			if wire1 == "exit" or wire2 == "exit" or wire3 == "exit":
				sys.exit()

            # Checks if the wires are cut in the correct order
			if wire1 == "red" and wire2 == "yellow" and wire3 == "blue":
				self.solved = True
				print("Correct! The lights are disabled, and the security system is down.")
				break
			else:
				attempts += 1
				print("Incorrect wire cutting sequence. The lights remain on.")
				if attempts == 2 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: The wires are in the order of colors commonly seen in traffic lights.")
						hint_given = True
				elif attempts == 3:
					print("You've failed to solve it. The security system is now aware of your presence.")
        


		"""print("The lights are flickering, you need to cut the right wires to disarm the security system")
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
			print("Incorrect wire cutting sequence. The lights remain on, security may be on the way")"""
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
			
			timer_answer = ((f"\n{timer}> Answer: "))

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


		hint_given = False  # Track if a hint has been given
		attempts = 0 # this trakcs the number of incorrect attempts

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
				attempts += 1
				self.solved = False
				break
			else:
				print("Good connection! ✔️")
				self.solved = True
				
		if self.solved:
			print("⚡Power successfully rerouted! ⚡")
		else:
			print("No successful connections. The power remains unstable")
			for attempt in range(3):
				if attempt == 2 and not hint_given:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						print("Hint: Look for the prime number pairs that match the given node")
						hint_given = True
						#break


		"""for nodes in nodes_key:
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
			print("⚡Power successfully rerouted! ⚡")"""
		return self.solved

# Maintenance Shaft Puzzles

class MovingPlatformPuzzle(Puzzle):

	input_interval = 0

	def timer_time(self, stop, t_id):
		global input_interval
		interval = 0

		#print(f"Starting thread {t_id}")

		while True:
			if stop():
				break

			interval_answer = ((f"\n> Interval {interval % 4 + 1}: "))

			print(interval_answer, end="")
				
			time.sleep(1)
			interval += 1
			input_interval = interval

	def run_puzzle(self):
		global input_interval

		print(f"{self.name}")
		print(f"{self.description}")

		print("You must time your jumps to the specified interval to avoid falling.")

		intervals = [1, 2, 3, 4]
		jump_count = 0
		platform_num = 4

		for i in range(platform_num):

			interval = random.choice(intervals)
			print(f"Enter 'j' to jump at interval {interval}")
			time.sleep(1.5)

			# threading setup
			t_id = i
			stop_thread = False
			threading1 = threading.Thread(target=self.timer_time, args=(lambda: stop_thread, t_id))
			threading1.daemon = True
			threading1.start()

			answer = input().lower()
			input_interval = input_interval % 4 + 1
			jump_cmd = "j"

			if interval != input_interval and answer != jump_cmd:
				print("Bad input and wrong interval! ❌")
				break
			elif answer != jump_cmd:
				print("Bad input! ❌")
				break
			elif interval != input_interval:
				print("Wrong interval! Try again! ❌")
				break
			elif answer == jump_cmd and interval == input_interval:
				print(f"You jumped on platform: {i + 1}.")
				print(f"{platform_num - i - 1} more! 🦘")
				jump_count += 1

			stop_thread = True
			threading1.join()
			input_interval = 0

		# Check if all inputs where correct
		if jump_count == platform_num:
			self.solved = True
			print(" 🦘 You made it across! 🦘")

		# Remember to stop and join the thread
		stop_thread = True
		threading1.join()

		return self.solved
	
class DeactivationPuzzle(Puzzle):
	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		# list of possible words
		words_list = ["guard", "escape", "diamond", "government"]

		# chooses a random word and scrambles it
		correct_word = random.choice(words_list)
		scrambled_word = list(correct_word)
		random.shuffle(scrambled_word)
		scrambled_word = "".join(scrambled_word)

		print(f"You see a scrambled code on the control panel: {scrambled_word}")

		# allows the player up to 3 attempts
		for attempt in range(3):
			player_input = input("Enter the correct word to deactivate the barriers: ").lower()

			if player_input == correct_word:
				print("The barriers deactivate. You can proceed!")
				self.solved = True #marks the puzzle as solved
				return True
			else:
				print("Incorrect. Try again")

				# offers a hint after the second failt attempt
				if attempt == 1:
					hint = input("Do you want a hint? (yes/no): ").lower()
					if hint == "yes":
						hint_letters = correct_word[:2] #this shows the first 2 letters
						print(f"Hint: The first two letters are '{hint_letters}' .")
				if attempt == 2:
					print("You failed to solved the puzzle. The barriers remain active")
					return False
		return self.solved


		#return super().run_puzzle()
	
class RapidRiddles(Puzzle):
	def timer_time(self, stop):
		countdown_time = 60

		while countdown_time:
			if stop():
				return  # Stop immediately if flagged
			
			mins, secs = divmod(countdown_time, 60)
			print(f"\n{mins:02d}:{secs:02d}> Answer: ", end="", flush=True)
			
			time.sleep(2)  # Simulate timer ticking
			countdown_time -= 1

		# If the countdown reaches zero, set self.solved to False and mark time as up
		self.solved = False
		self.time_up = True
		print("\nTime's up! You can't answer now.")

	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		self.riddles = ["rodiamondugh","Goooooooooooooooo","the weather\nfeeling"] 
		self.answers = ["diamond in the rough", "go long","feeling under the weather"]
		self.answered = 0

		self.solved = False  # Ensure default state
		self.time_up = False  # Track whether time has expired

		stop_thread = False
		timer_thread = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
		timer_thread.daemon = True
		timer_thread.start()

		# Stop input if time runs out
		while not self.time_up:
			print(self.riddles[self.answered])
			answer = input("Answer (or type 'hint' for a clue): ").lower()

			if self.time_up:  # Double check after input to prevent late answers
				print("Time is already up! Too late.")
				break

			if answer == "exit":
				stop_thread = True
				sys.exit()

			elif answer == "hint":
				print("Hint: Think about common sayings or phrases related to the riddle.")
				continue

			elif answer == self.answers[self.answered]:
				self.solved = True
				print("That riddle is solved.")
				self.answered += 1
				if self.answered == 3:
					print("You have solved the puzzle.")
					break  # Stop waiting for input
			else:
				print("Incorrect. :(")

		stop_thread = True  # Ensure the timer stops
		timer_thread.join()

		"""while not self.time_up:
			print(self.riddles[self.answered])
			answer = input().lower()

			

			if self.time_up:  # Double check after input to prevent late answers
				print("Time is already up! Too late.")
				break

			if answer == "exit":
				stop_thread = True
				sys.exit()

			elif answer == self.answers[self.answered]:
				self.solved = True
				print("That riddle is solved.")
				self.answered += 1
				if( self.answered == 3):
					print("You have solved the puzzle.")
					break  # Stop waiting for input
			
			else:
				print("Incorrect. :(")
				break  # Stop waiting for input

		stop_thread = True  # Ensure the timer stops
		timer_thread.join()"""

		return self.solved  # Always return self.solved
	
class guessThatSong(Puzzle):
	def timer_time(self, stop):
		countdown_time = 30

		while countdown_time:
			if stop():
				return  # Stop immediately if flagged
			
			mins, secs = divmod(countdown_time, 60)
			print(f"\n{mins:02d}:{secs:02d}> Answer: ", end="", flush=True)
			
			time.sleep(2)  # Simulate timer ticking
			countdown_time -= 1

		# If the countdown reaches zero, set self.solved to False and mark time as up
		self.solved = False
		self.time_up = True
		print("\nTime's up! You can't answer now.")

	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")

		print("oscysbtdelwspwhattlgwbsabsttpfotrwwwsgsatrrgtbbiagpttntofwstosdtsbywotlotfathotb")

		self.solved = False  # Ensure default state
		self.time_up = False  # Track whether time has expired

		stop_thread = False
		timer_thread = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
		timer_thread.daemon = True
		timer_thread.start()

		# Stop input if time runs out
		while not self.time_up:
			answer = input("Answer (or type 'hint' for a clue): ").lower()

			if self.time_up:  # Double check after input to prevent late answers
				print("Time is already up! Too late.")
				break

			if answer == "exit":
				stop_thread = True
				sys.exit()
			elif answer == "hint":
				print("Hint: It's a patriotic song, often sung at sporting events.")
				continue

			elif answer == "the star spangled banner":
				self.solved = True
				print("You have solved the puzzle.")
				break  # Stop waiting for input
			else:
				print("Incorrect. :(")
		stop_thread = True  # Ensure the timer stops
		timer_thread.join()
		"""while not self.time_up:
			
			answer = input().lower()

			if self.time_up:  # Double check after input to prevent late answers
				print("Time is already up! Too late.")
				break

			if answer == "exit":
				stop_thread = True
				sys.exit()

			elif answer == "the star spangled banner":
				self.solved = True
				print("You have solved the puzzle.")
				break  # Stop waiting for input
			
			else:
				print("Incorrect. :(")
				break  # Stop waiting for input

		stop_thread = True  # Ensure the timer stops
		timer_thread.join()"""

		return self.solved  # Always return self.solved
	

class weightExchange(Puzzle):

	def timer_time(self, stop):
		countdown_time = 15

		while countdown_time:
			if stop():
				return  # Stop immediately if flagged
			
			mins, secs = divmod(countdown_time, 60)
			print(f"\n{mins:02d}:{secs:02d}> Answer: ", end="", flush=True)
			
			time.sleep(2)  # Simulate timer ticking
			countdown_time -= 1

		# If the countdown reaches zero, set self.solved to False and mark time as up
		self.solved = False
		self.time_up = True
		print("\nTime's up! You can't answer now.")

	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")
		print("(Guess the number and it will tell you higher or lower.)")

		self.solved = False  # Ensure default state
		self.time_up = False  # Track whether time has expired

		stop_thread = False
		timer_thread = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
		timer_thread.daemon = True
		timer_thread.start()

		# Stop input if time runs out
		while not self.time_up:
			answer = input("\n> Answer: ").lower()

			try:
				answer = int(answer)
			except:
				print("Bad input! ❌")

			if int(answer) == 5:
				self.solved = True
				print("You have solved the puzzle.")
				break

			elif int(answer) < 5:
				print("Higher")
			elif int(answer) > 5:
				print("Lower")

			else:
				print("Incorrect. :(")

		stop_thread = True  # Ensure the timer stops
		timer_thread.join()
		return self.solved
	

class escapeHatchHack(Puzzle):

	def timer_time(self, stop):
		countdown_time = 15

		while countdown_time:
			if stop():
				return  # Stop immediately if flagged
			
			mins, secs = divmod(countdown_time, 60)
			print(f"\n{mins:02d}:{secs:02d}> Answer: ", end="", flush=True)
			
			time.sleep(2)  # Simulate timer ticking
			countdown_time -= 1

		# If the countdown reaches zero, set self.solved to False and mark time as up
		self.solved = False
		self.time_up = True
		print("\nTime's up! You can't answer now.")

	def run_puzzle(self):
		print(f"{self.name}")
		print(f"{self.description}")
		print("8 X 5 / (8 + 2)")


		self.solved = False  # Ensure default state
		self.time_up = False  # Track whether time has expired

		stop_thread = False
		timer_thread = threading.Thread(target=self.timer_time, args=(lambda: stop_thread,))
		timer_thread.daemon = True
		timer_thread.start()

		# Stop input if time runs out
		while not self.time_up:
			answer = input("\n> Answer: ").lower()

			try:
				answer = int(answer)
			except:
				print("Bad input! ❌")

			if int(answer) == 4:
				self.solved = True
				print("You have solved the puzzle.")
				break

			else:
				print("Incorrect. :(")
				
		stop_thread = True  # Ensure the timer stops
		timer_thread.join()
		return self.solved