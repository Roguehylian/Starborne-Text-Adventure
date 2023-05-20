# Python Text RPG
# By: Matthew Mendoza

import cmd
import textwrap
import sys
import os
import time 
import random

screen_width = 100

##### Player Setup #####
class player:
	def __init__(self):
		self.name = ''
		self.location = 'b2'
		self.game_over = False

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
	print('# Welcome to the Text RPG! #')
	print('############################')
	print('         - Play -           ')
	print('         - Help -           ')
	print('         - Quit -           ')
	title_screen_selections()

def help_menu():
	print('############################')
	print('# Welcome to the Text RPG! #')
	print('############################')
	print('- Use up, down, left, right to move -')
	print('- Type your commands to do them -')
	print('- Use "Look" to inspect something -')
	print('- Good luck and have fun! -')
	title_screen_selections()




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

solved_places = {'a1': False,'a2': False,'a3': False,'a4': False,
				'b1': False,'b2': False,'b3': False,'b4': False,
				'c1': False,'c2': False,'c3': False,'c4': False,
				'd1': False,'d2': False,'d3': False,'d4': False,
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
		RIGHT :'a4',
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
		ZONENAME: "Home",
		DESCRIPTION : 'This is your home!',
		EXAMINATION : 'examine',
		SOLVED : False,
		UP : 'a2',
		DOWN : 'c2',
		LEFT : 'b1',
		RIGHT : 'b3',
	},
	'b3': {
		ZONENAME: "",
		DESCRIPTION : 'description',
		EXAMINATION : 'Your home looks the same - nothing has changed.',
		SOLVED : False,
		UP : 'a3',
		DOWN : 'c3',
		LEFT : 'b2',
		RIGHT : 'b4',
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
		RIGHT : 'c4',
	},
}	



#### GAME INTERACTIVITY ####
def print_location():
	print(f"{zonemap[myPlayer.location][DESCRIPTION]}")


def prompt():
	print(f"\n================================")
	print("What would you like to do?")
	print("Valid actions: Move, Examine, Quit")
	action = input ("> ")
	acceptable_actions = ['move','examine','quit']
	while action.lower() not in acceptable_actions:
		print("Unknown action, try again\n")
		action = input("> ")
	if action.lower() == "quit":
		sys.exit()
	elif action.lower() in ['move','go', 'travel','walk']:
		player_move(action.lower)
	elif action.lower() in ['examine','inspect','interact','look']:
		player_examine(action.lower())

def player_move(myAction):
	dest = input("Where would you like to move to?\nValid options are up/north, down/south, right/east, left/west\n")
	if dest in ['up','north']:
		if destination == '':
			print("oops, you can't go there.")
			player_move
		destination = zonemap[myPlayer.location][UP]
		movement_handler(destination)
	elif dest in ['down','south']:
		if destination == '':
			print("oops, you can't go there.")
			player_move
		destination = zonemap[myPlayer.location][DOWN]
		movement_handler(destination)
	elif dest in ['right','east']:
		if destination == '':
			print("oops, you can't go there.")
			player_move
		destination = zonemap[myPlayer.location][RIGHT]
		movement_handler(destination)
	elif dest in ['left','west']:
		if destination == '':
			print("oops, you can't go there.")
			player_move
		destination = zonemap[myPlayer.location][LEFT]
		movement_handler(destination)



def movement_handler(destination):
	print(f"You have moved to {destination}.")
	myPlayer.location = destination
	print_location()

def player_examine(action):
	if zonemap[myPlayer.location][SOLVED]:
		print("You have already solved this puzzle.")
	else:
		##### Puzzle goes here.
		print("You a trigger a puzzle here.")


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





















