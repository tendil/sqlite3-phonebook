"""Module for contacts table management for each user."""

from prettytable import PrettyTable
import sqlite3
import csv
import re

from utils import user, helper

# Global sqlite3 connection and cursor
conn = sqlite3.connect('material.db')
c = conn.cursor()

# Name of current table
_tablename = ''


def _verify_contact_name(name):
	"""Fails if contact name isn't valid."""
	if re.fullmatch('[a-zA-Z ]*[а-яА-Я ]*', name) is None:
		print('\n\033[48;5;88mError: Invalid contact name\033[0;0m')
		return False


def _verify_contact_num(num):
	"""Fails if contact number isn't valid."""
	if re.fullmatch('''[+]?\d{0,3}[ ]?\d{10}''', num) is None:
		print('\n\033[48;5;88mError: Invalid contact number\033[0;0m')
		return False


# ^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$
def _verify_contact_email(email):
	"""Fails if contact email is not valid."""
	if re.search('''[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,6}''', email) is None:
		print('\n\033[48;5;88mError: Invalid contact email\033[0;0m')
		return False


def _set_tablename(username):
	# Allows changing the value of global var tablename
	global _tablename
	"""Sets tablename based on the username obtained from user module."""
	_tablename = 'contacts_' + username
	# Tablename sanitized to avoid SQL injection attacks
	_tablename = user.helper.scrub(_tablename)


def show_all_contacts():
	"""Shows all contacts in a user's contact table along with the total contact count."""
	print('~' * 20, '\033[38;5;63m\nShowing all contacts\033[0;0m\n' + '~' * 20)

	contact_count = c.execute(f'SELECT COUNT(*) FROM {_tablename}').fetchone()[0]
	print(f'\033[48;5;22m\nTotal Contact Count: {contact_count}\033[0;0m\n')

	conclusion = PrettyTable()
	for name, phno, email in c.execute(f'SELECT name, phno, email FROM {_tablename}'):
		conclusion.field_names = ['Full name', 'Number', 'Email address']
		conclusion.add_row([name, phno, email])
		conclusion.sortby = 'Full name'
	print(conclusion)


def add_contact():
	"""Adds a contact to the contacts table.
	Input is validated using Regex matching
	"""
	print('~' * 11, '\n\033[38;5;63mAdd contact\033[0;0m\n' + '~' * 11)
	contact_list = list()

	# contact name
	contact_name = input('\nName: ')
	if _verify_contact_name(contact_name) is False:
		return False
	else:
		contact_list.append(contact_name)

	# contact number
	contact_num = input('\nNumber: ')
	# '+' may or may not appear in start of the number
	# country code may or may not appear (0 to 3 digits)
	# a ' ' may or mat not appear
	# 10 digits must appear
	if _verify_contact_num(contact_num) is False:
		return False
	else:
		contact_list.append(contact_num)

	# contact email
	contact_email = input('\nEmail: ')
	if contact_email == '':
		contact_email = 'NULL'
		contact_list.append(contact_email)
	# Copied from GfG
	elif _verify_contact_email(contact_email) is False:
		return False
	else:
		contact_list.append(contact_email)

	contact_tuple = tuple(contact_list)
	try:
		# insert the value in username table
		c.execute(f'''INSERT INTO {_tablename} 
						VALUES (?, ?, ?);''', contact_tuple)
		conn.commit()
		return True
	except:
		print('\n\033[48;5;88mHere in except\033[0;0m\n')
		return False


def modify_contact():
	"""Modify contact based on the user's choice."""
	print('~' * 17, '\n\033[38;5;63mModifying contact\033[0;0m\n' + '~' * 17)
	contact_name = ''

	while contact_name == '' or contact_name == ' ':
		contact_name = input('\nEnter name of contact to modify: ')

	if c.execute(f'''SELECT * FROM {_tablename} WHERE LOWER(name) = ?''', (contact_name.lower(),)).fetchone() is None:
		return False

	modify_attribute = helper.select_attributes()

	if modify_attribute == 1:
		try:
			modified_name = input('\nEnter new name of contact: ')
			if _verify_contact_name(modified_name) is False:
				return False

			c.execute(f'''UPDATE {_tablename} 
							SET name = ?
							WHERE LOWER(name) = ?;''', (modified_name, contact_name.lower(),))
			conn.commit()
			return True
		except:
			return False

	elif modify_attribute == 2:
		try:
			modified_num = input('\nNumber: ')
			if _verify_contact_num(modified_num) is False:
				return False

			c.execute(f'''UPDATE {_tablename} 
							SET phno = ?
							WHERE LOWER(name) = ?;''', (modified_num, contact_name.lower(),))
			conn.commit()
			return True
		except:
			return False

	elif modify_attribute == 3:
		try:
			modified_mail = input('\nEmail: ')
			if modified_mail == '':
				modified_mail = 'NULL'
			elif _verify_contact_email(modified_mail) is False:
				return False

			c.execute(f'''UPDATE {_tablename} 
							SET email = ?
							WHERE LOWER(name) = ?;''', (modified_mail, contact_name.lower(),))
			conn.commit()
			return True
		except:
			return False


def delete_contact():
	"""Deletes contact based on the user input from the contacts table"""
	print('~' * 14, '\n\033[38;5;63mDelete contact\033[0;0m\n' + '~' * 14)
	delete_contact_name = ''

	while delete_contact_name == '' or delete_contact_name == ' ':
		delete_contact_name = input('\nEnter name of contact to delete: ')

	# If there's at least one entry in table with given key name, then delete it
	if c.execute(f'''SELECT * FROM {_tablename} WHERE LOWER(name) = ?''',
				 (delete_contact_name.lower(),)).fetchone() is not None:
		query = c.execute(f'''DELETE FROM {_tablename}
							WHERE LOWER(name) = ?''', (delete_contact_name.lower(),))
		conn.commit()
		return True
	else:
		return False


def search_contact():
	"""Searches a contact in the current table and prints all relevant matches."""
	print('~' * 14, '\n\033[38;5;63mSearch contact\033[0;0m\n' + '~' * 14)
	print('\n\033[38;5;212mEnter Name to search the contact...\033[0;0m')
	name_key = input('\nName: ')

	while name_key == '' or name_key == ' ':
		print('\033[48;5;88mNo input..\ntry again:\033[0;0m ')
		name_key = input('\nName: ')

	# flag
	flag = False
	for contact_name, number, email in c.execute(f'SELECT * FROM {_tablename}'):
		if name_key.lower() == contact_name.lower():
			print(f'Name: {contact_name} | Number: {number} | Email: {email}')
			flag = True

	return flag


def import_csv():
	"""Imports a CSV from the current directory and stores the data into table.

	Assuming the CSV will be in the following format: name,number,email
	"""
	print('~' * 10, '\n\033[38;5;63mImport CSV\033[0;0m\n' + '~' * 10)
	filename = ''
	while filename == '' or filename == ' ':
		filename = input('\n\033[38;5;212mEnter filename (must be in current directory, phonebook/):\033[0;0m ')

	try:
		with open(filename, 'r') as file:
			csv_reader = csv.reader(file)
			for row in csv_reader:
				print(row)
				# If either name or number is empty, fail the operation
				if row[0] == '' or row[1] == '':
					print('\033[48;5;88mHere\033[0;0m')
					return False
				# if email doesn't exist
				if len(row) == 2:
					row.append('NULL')
				c.execute(f'''INSERT INTO {_tablename} 
								VALUES (?, ?, ?)''', tuple(row))
			else:
				conn.commit()
				return True
	except:
		return False


def export_csv():
	"""Exports contents of table to a csv file in the current directory. Input name from user."""
	print('~' * 10, '\n\033[38;5;63mExport CSV\033[0;0m\n' + '~' * 10)
	filename = ''

	# Read the CSV filename while handling incorrect inputs
	while filename.isalnum() is False and '.' not in filename:
		filename = input('\n\033[38;5;212mCSV filename:\033[0;0m ')
		if filename.isalnum() is False and '.' not in filename:
			print('\n\033[48;5;88mError: Invalid filename. Try again!\033[0;0m\n')

	try:
		with open(filename, 'w') as file:
			csv_writer = csv.writer(file)
			for row in c.execute(f'SELECT * FROM {_tablename}'):
				csv_writer.writerow(row)
			else:
				return True
	except:
		return False
