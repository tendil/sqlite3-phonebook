"""Module provides various helper functions for main script and other modules."""

import os
import sys
import time
from enum import Enum

# from phonebook import _user_management
# from utils.prints import PrintFailed as PF, ContactSuccessfully as CS
# from utils import contacts as c


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
	return ''.join(clr for clr in table_name if clr.isalnum() or clr == '_')


def select_attributes():
	"""Returns user selected column"""
	attrib = """
		\033[38;5;212mWhich attribute you want to change.\033[0;0m
		 1. Name
		 2. Phone Number
		 3. Email
	"""
	print(attrib)

	choice = int(input('\n\033[48;5;88mInput choice:\033[0;0m\n '))

	clear_screen()
	if choice < 1 or choice > 4:
		raise Exception('\n\033[48;5;88mInvalid choice\033[0;0m\n')
	else:
		return choice


class MenuUser(Enum):
	ADD_USER = 1
	DELETE_USER = 2
	SELECT_USER = 3
	EXIT = 0


class MenuContacts(Enum):
	ALL_CONTACTS = 1
	ADD_CONTACT = 2
	DELETE_CONTACT = 3
	SEARCH_CONTACT = 4
	MODIFY_CONTACT = 5
	IMPORT_CSV = 6
	EXPORT_CSV = 7
	USER_MANAGEMENT = 8
	EXIT = 9
