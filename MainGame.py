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
	print('############################')
	print('#   Welcome to Starborne!  #')
	print('############################')
	print('         - Play -           ')
	print('         - Help -           ')
	print('         - Quit -           ')
	title_screen_selections()

def help_menu():
	print('############################')
	print('#   Welcome to Starborne!  #')
	print('############################')
	print('- Use up, down, left, right to move -')
	print('- Type your commands to do them -')
	print('- Use "Examine" to inspect something -')
	print('- Good luck and have fun! -')
	title_screen()




#def exam_a1():
#	question = input("Hello, what's 1+1?")
#	if question == 2:
#		return


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
		ZONENAME: "Town Market",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : '',
		DOWN : 'b1',
		LEFT : '',
		RIGHT : 'a2'
	},
	'a2': {
		ZONENAME: "Town Entrance",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP :'',
		DOWN : 'b2',
		LEFT : 'a1',
		RIGHT : 'a3',
	},
	'a3': {
		ZONENAME: "Town Square",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : '',
		DOWN : 'b3',
		LEFT : 'a2',
		RIGHT :'',
	},
	'b1': {
		ZONENAME: "",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : 'a1',
		DOWN : 'c1',
		LEFT : '',
		RIGHT : 'b2',
	},
	'b2': {
		ZONENAME: "Center",
		DESCRIPTION : 'The remains of your ship lay on the ground.',
		EXAMINATION : 'examine',
		SOLVED : True,
		UP : 'a2',
		DOWN : 'c2',
		LEFT : 'b1',
		RIGHT : 'b3',
	},
	'b3': {
		ZONENAME: "",
		DESCRIPTION : 'A ghost appears in front of you',
		EXAMINATION : 'The spooky lad asks: what is 1+1?',
		SOLVED : 2,
		UP : 'a3',
		DOWN : 'c3',
		LEFT : 'b2',
		RIGHT : '',
	},
	
	'c1': {
		ZONENAME: "",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : 'b1',
		DOWN : '',
		LEFT : '',
		RIGHT : 'c2',
	},
	'c2': {
		ZONENAME: "",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : 'b2',
		DOWN : '',
		LEFT : 'c1',
		RIGHT : 'c3',
	},
	'c3': {
		ZONENAME: "",
		DESCRIPTION : 'description',
		EXAMINATION : 'examine',
		SOLVED : False,
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
	if myPlayer.location == 'b2':
		if myPlayer.solves >= 8:
			print("As you return to your ship, the door in front of you unlocks, showing you a vast field full of monsters and unknown minerals. Perhaps you can explore this world after all.")
			print("\nCONGRATULATIONS!")
			sys.exit()
		else:
			print("Nothing seems to be happening...")
	elif myPlayer.location == 'b3':
		if puzzle_answer == str((zonemap[myPlayer.location][SOLVED])):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")
		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
	else:
		if puzzle_answer == (zonemap[myPlayer.location][SOLVED]):
			rooms_solved[myPlayer.location] = True
			myPlayer.solves += 1
			print("You have solved the puzzle. Onwards!")
			print(f"\nOrbs collected: {str(myPlayer.solves)}/8")

		else:
			print("Wrong answer! Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
			player_examine()
		



def movement_handler(destination):
	print(f"You have moved to {destination}.")
	myPlayer.location = destination
	print_location()

def player_examine():
	if rooms_solved[myPlayer.location] == False:
		print(zonemap[myPlayer.location][EXAMINATION])
		puzzle_answer = str(input())
		checkpuzzle(puzzle_answer)
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
	main_game_loop()

title_screen()





















