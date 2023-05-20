# Python Text RPG
# By: Matthew Mendoza

import cmd
import textwrap
import sys
import os
import time 
import random

##### Player Setup #####
class player:
	def __init__(self):
		self.name = ''
		self.location = 'b2'
		self.game_over = False
		self.solves = 0 #There are 8 puzzles.


myPlayer = player()


#### Title Screen ####m
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		setup_game() #placeholder until written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play','help','quit']:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
			setup_game() #placeholder until written
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	print('''
   ____                  _                             
 / _____) _              | |                            
( (____ _| |_ _____  ____| |__   ___   ____ ____  _____ 
 \____ (_   _|____ |/ ___)  _ \ / _ \ / ___)  _ \| ___ |
 _____) )| |_/ ___ | |   | |_) ) |_| | |   | | | | ____|
(______/  \__)_____|_|   |____/ \___/|_|   |_| |_|_____)

                	- Play -           
	                - Help -           
	                - Quit -           

''')
	title_screen_selections()

def help_menu():
	print('- Use up, down, left, right to move -')
	print('- Type your commands to do them -')
	print('- Use "Examine" to inspect something -')
	print('- Good luck and have fun! -')
	title_screen()





#### MAP #### 

#a1,a2... # PLAYER STARTS AT b2


#----------
#|  |  |  |
#----------
#|  |  |  |
#----------
#|  |  |  |
#----------


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up','north'
DOWN = 'down','south'
LEFT = 'left','west'
RIGHT = 'right','east'

rooms_solved = {'a1': False,'a2': False,'a3': False,
				'b1': False,'b2': False,'b3': False,
				'c1': False,'c2': False,'c3': False,
				}

zonemap = {
	'a1': {
		ZONENAME: "Rock Candy Cat Room",
		DESCRIPTION : 'A cat made out of rock candy looks at you curiously.',
		EXAMINATION : 'The cat licks its paws and says: I am unique like a snowflake, hard as a rock. I refract like a diamond, and am found in a block. What am I?',
		SOLVED : 'crystal',
		UP : '',
		DOWN : 'b1',
		LEFT : '',
		RIGHT : 'a2'
	},
	'a2': {
		ZONENAME: "Grand Gate Room",
		DESCRIPTION : 'A large purple gate stands in your path.',
		EXAMINATION : '',
		SOLVED : False,
		UP :'examine',
		DOWN : 'b2',
		LEFT : 'a1',
		RIGHT : 'a3',
	},
	'a3': {
		ZONENAME: "Meek Mouse Room",
		DESCRIPTION : 'A meek mouse comes up to you and crawls up your body, making its way up to your head.',
		EXAMINATION : "The mouse hangs from its tail, inches away from your face. It says: what has 12 legs, six eyes, three tails, and can't see?",
		SOLVED : 'three blind mice',
		UP : '',
		DOWN : 'b3',
		LEFT : 'a2',
		RIGHT :'',
	},
	'b1': {
		ZONENAME: "Blightful Book Room",
		DESCRIPTION : 'A tattered book coughs and wheezes as it tries to catch its breath.',
		EXAMINATION : '''Through coughs, it manages to ask: I am but the product of another man's image. For centuries I stand, though I too wither with age. People from around the world come to spectate my visage. Though I speak no words of wisdom, I give them all my knowledge. I am a:''',
		SOLVED : 'statue',
		UP : 'a1',
		DOWN : 'c1',
		LEFT : '',
		RIGHT : 'b2',
	},
	'b2': {
		ZONENAME: "Curious Center Room",
		DESCRIPTION : 'You see a small insect emerge from the rubble, spreading its wings and taking flight.',
		EXAMINATION : 'The small insect suprinsingly clears its throat and says: You see me blink but not my eyes, I wink and wink to fraternize, And if I wink at her just right, Then I may find my love tonight. What am I?',
		SOLVED : 'firefly',
		UP : 'a2',
		DOWN : 'c2',
		LEFT : 'b1',
		RIGHT : 'b3',
	},
	'b3': {
		ZONENAME: "Ghastly Ghost Room",
		DESCRIPTION : "A haunting ghost appears in front of you, barring its frightful jagged teeth.",
		EXAMINATION : "The spooky lad asks: When I'm young I'm tall. When I'm old I'm short. When I'm alive I glow. Because of your breath I die. I am a:",
		SOLVED : "candle",
		UP : 'a3',
		DOWN : 'c3',
		LEFT : 'b2',
		RIGHT : '',
	},
	
	'c1': {
		ZONENAME: "Chatty Chime Room",
		DESCRIPTION : 'As you enter the room, a gust of wind comes in. A talking chime blabbers on about something.',
		EXAMINATION : 'Its chimes stop. It asks: I am what is produced by rapid movements in the air which create sound. What am I?',
		SOLVED : 'vibrations',
		UP : 'b1',
		DOWN : '',
		LEFT : '',
		RIGHT : 'c2',
	},
	'c2': {
		ZONENAME: "Lizard in a blizzard room",
		DESCRIPTION : 'You are met with a chilling breeze that makes both you and a small lizard shiver.',
		EXAMINATION : 'Through chattering teeth, it asks: What bites without teeth?',
		SOLVED : 'frost',
		UP : 'b2',
		DOWN : '',
		LEFT : 'c1',
		RIGHT : 'c3',
	},
	'c3': {
		ZONENAME: "Condescending Canvas Room",
		DESCRIPTION : 'A canvas with beautiful art looks at you with disgust.',
		EXAMINATION : '''It scoffs, not even bothering to look at you. It says: I’m sometimes used with canvas but I’m not a tent. I’m used with a brush but I’m not toothpaste. What am I ?''',
		SOLVED : 'paint',
		UP : 'b3',
		DOWN : '',
		LEFT : 'c2',
		RIGHT : '',
	},
}	



#### GAME INTERACTIVITY ####
def print_location():
	print(f"{zonemap[myPlayer.location][DESCRIPTION]}")


def prompt():
	print(f"\n================================")
	print("What would you like to do?")
	print("Valid actions: Move, Examine, Map, Quit")
	action = input ("> ")
	acceptable_actions = ['move','examine','map','quit']
	while action.lower() not in acceptable_actions:
		print("Unknown action, try again.\n")
		action = input("> ")
	if action.lower() == "quit":
		sys.exit()
	elif action.lower() in ['move','go', 'travel','walk']:
		player_move(action.lower)
	elif action.lower() in ['examine','inspect','interact','look']:
		player_examine()
	elif action.lower() == 'map':
		player_map()

def player_move(myAction):
	dest = input("Where would you like to move to?\nValid options are up/north, down/south, right/east, left/west\n")
	if dest in ['up','north']:
		destination = zonemap[myPlayer.location][UP]
		if destination == '':
			print("Oops, you can't go there.")
			player_move(myAction)
		else:
			movement_handler(destination)

	elif dest in ['down','south']:
		destination = zonemap[myPlayer.location][DOWN]
		if destination == '':
			print("oops, you can't go there.")
			player_move(myAction)
		else:
			movement_handler(destination)


	elif dest in ['right','east']:
		destination = zonemap[myPlayer.location][RIGHT]
		if destination == '':
			print("oops, you can't go there.")
			player_move(myAction)
		else:
			movement_handler(destination)


	elif dest in ['left','west']:
		destination = zonemap[myPlayer.location][LEFT]
		if destination == '':
			print("oops, you can't go there.")
			player_move(myAction)
		else:
			movement_handler(destination)




def checkpuzzle(puzzle_answer):
	### GATE ROOM CHECK
	if myPlayer.location == 'a2':
		if myPlayer.solves >= 8:
			print("As you return to the gate, the orbs you collected merge into one, forming the mythical shadow crystal. The gate opens, showing you a vast field full of monsters and unknown minerals. Perhaps you can explore this world after all.")
			print("\nCONGRATULATIONS! YOU WIN!")
			sys.exit()
		else:
			print("You try to open the gate, but it doesn't budge.")

	elif myPlayer.location == 'a1':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()

	elif myPlayer.location == 'a3':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()

	elif myPlayer.location == 'b1':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	elif myPlayer.location == 'b2':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	elif myPlayer.location == 'b3':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	elif myPlayer.location == 'c1':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	elif myPlayer.location == 'c2':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	elif myPlayer.location == 'c3':
		if puzzle_answer.lower() == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()







		


#################################################################################################

def movement_handler(destination):
	print(f"You have moved to {destination}.")
	myPlayer.location = destination
	print_location()

def player_examine():
	if rooms_solved[myPlayer.location] == False:
		if myPlayer.location != 'a2':
			print(zonemap[myPlayer.location][EXAMINATION])
			puzzle_answer = str(input())
			checkpuzzle(puzzle_answer)
		else:
			checkpuzzle('None')
	else:
		print("There is nothing new for you to see here.")

def player_map():
	print(f'''
You are currently at: {myPlayer.location }
----------
|a1|a2|a3|
----------
|b1|b2|b3|
----------
|c1|c2|c3|
----------''')


#### GAME FUNCTIONALITY ####
def main_game_loop():
	while myPlayer.game_over is False:
		prompt()


def setup_game():
	player_name = input("Hello, what's your name?\n")
	myPlayer.name = player_name
	print(f"Let's start, {player_name}!")
	print('''
The commander sent us out to explore the planet of darkness, code named "Nyxis", named after the goddess of night, Nyx. We trained for years,
preparing for this one mission. Me, alongside my fellow colonizers, blasted into the starry galaxy in hopes of finding a Shadow Crystal. These
crystals are said to be husks of former absolute might, a capsule that once held incredible power. gazing in awe at the ominous planet. Its
purple haze pulsed, emitting a low, dull hum. All of a sudden, we lost total control of the ship. Its ominous sound only grew louder the closer
we got to the planet. Clouds of violet fogged our vision as we dived straight towards the planet, until all we could see was darkness. I opened
my eyes, only to find my entire team dead from the crash.. My body ached with pain, but.. I saw no injuries on myself. Still dazed, I walked
towards the murky cave with my flashlight, confusion and fear stirring within me.''')
	print("\nYou see a small insect emerge from the rubble, spreading its wings and taking flight.")
	main_game_loop()

title_screen()