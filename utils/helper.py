"""Module provides various helper functions for main script and other modules."""

import sys
import time
import os
# import keyboard
# import phonebook

# def back_to_menu():
# 	"""Returns the user to the main menu. Useful for the wrong choice"""
# 	 keyboard.add_hotkey("ctrl+alt+a", phonebook._input_contact_menu_choice())
# 	keyboard.wait("ctrl + b")
# 	return phonebook._contacts_management()

def clear_screen():
	"""Clears the screen after switching menu"""
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')


def trigger_exit():
	"""Initiates the exit sequence."""
	print('\nExiting phonebook! Bye!')
	time.sleep(0.3)
	sys.exit(1)


def scrub(table_name):
	"""Sanitizes input for database query"""
	return ''.join(chr for chr in table_name if chr.isalnum() or chr == '_')


def select_attributes():
	"""Returns user selected column"""
	print('\n\033[38;5;212mWhich attribute you want to change.\033[0;0m\n')
	print('1. Name')
	print('2. Phone Number')
	print('3. Email\n')
	choice = int(input('\n\033[48;5;88mInput choice:\033[0;0m\n '))

	clear_screen()
	if choice < 1 or choice > 4:
		raise Exception('\n\033[48;5;88mInvalid choice\033[0;0m\n')
	else:
		return choice

