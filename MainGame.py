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
		self.hp = 0
		self.mp = 0
		self.status_effects [0]
		self.location = 'start'

myPlayer = player()


#### Title Screen ####
def title_screen_selections():
	option = input("> ")
	if option.lower() == ("play"):
		start_game() #placeholder until written
	elif option.lower() == ("help"):
		help_menu()
	elif option.lower() == ("quit"):
		sys.exit()
	while option.lower() not in ['play','help','quit']:
		print("Please enter a valid command.")
		option = input("> ")
		if option.lower() == ("play"):
			start_game() #placeholder until written
		elif option.lower() == ("help"):
			help_menu()
		elif option.lower() == ("quit"):
			sys.exit()

def title_screen():
	os.system('clear')
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





