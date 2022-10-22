"""Module provides various helper functions for main script and other modules."""

import sys
import time
import os

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
	print(
		'\n\033[38;5;212mWhich attribute you want to change.\033[0;0m\n'
		'\n1. Name\n'
		'2. Phone Number\n'
		'3. Email\n'
	)
	choice = int(input('\n\033[48;5;88mInput choice:\033[0;0m\n '))

	clear_screen()
	if choice < 1 or choice > 4:
		raise Exception('\n\033[48;5;88mInvalid choice\033[0;0m\n')
	else:
		return choice

