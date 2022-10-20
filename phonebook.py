"""phonebook is a simple contact management tool written in python."""

from utils import user
from utils import contacts
from utils import helper


def _input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print('~' * 20,'\n\033[38;5;63mUser Management Menu\033[0;0m\n' + '~' * 20)
	print('\n1. Add user')
	print('2. Delete user')
	print('3. Select user')
	print('0. Exit\n')

	choice = int(input('Input choice: '))
	helper.clear_screen()
	if choice < 1 or choice > 4:
		raise ValueError
	else:
		return choice


def _input_contact_menu_choice():
	"""Displays contact management options and returns user's input choice"""
	choice = 0
	print()
	print('~' * 23,'\n\033[38;5;63mContact Management Menu\033[0;0m\n' + '~' * 23)
	print('\n1. Show all contacts')
	print('2. Add contact')
	print('3. Delete contact')
	print('4. Search contact')
	print('5. Modify contact')
	print('6. Import CSV')
	print('7. Export CSV')
	print('8. Switch to user management mode')
	print('0. Exit\n')

	choice = int(input('Input choice: '))
	helper.clear_screen()
	if choice < 1 or choice > 9:
		raise ValueError
	else:
		return choice


def _user_management():
	"""Processes user management menu input"""
	# Redraw user management menu until a user is successfully selected
	try:
		while True:
			user_choice = _input_user_menu_choice()
			if user_choice == 1:
				if user.add_user() is True:
					print('\033[38;5;118m\nUser successfully added \033[0;0m\n')
				else:
					print('\033[48;5;88m\nError: user already exists \033[0;0m\n')
			elif user_choice == 2:
				if user.remove_user() is True:
					print('\033[38;5;118m\nUser successfully removed \033[0;0m\n')
				else:
					print('\033[48;5;88m\nError: user does not exist \033[0;0m\n')
			elif user_choice == 3:
				if user.select_user() is True:
					print('\033[38;5;118m\nUser successfully selected \033[0;0m\n')
					break
				else:
					print('\033[48;5;88m\nError: user does not exist \033[0;0m\n')
			else:
				helper.trigger_exit()
	except EOFError:
		_user_management()
	except ValueError:
		print('\033[48;5;88m\nError: Invalid Input. Please try again! \033[0;0m\n')
		_user_management()


def _contacts_management():
	"""Processes contact management menu input."""
	# Redraw contact management menu until user exits.
	try:
		while True:
			contacts_choice = _input_contact_menu_choice()
			if contacts_choice == 1:
				contacts.show_all_contacts()
			elif contacts_choice == 2:
				if contacts.add_contact() is True:
					print('\033[38;5;118m\nContact added successfully \033[0;0m')
				else:
					print('\033[48;5;88mCould not add contact!\033[0;0m')
			elif contacts_choice == 3:
				if contacts.delete_contact() is True:
					print('\033[38;5;118m\nContact deleted successfully\033[0;0m')
				else:
					print('\033[48;5;88m\nContact not found!\033[0;0m')
			elif contacts_choice == 4:
				if contacts.search_contact() is False:
					print('\033[48;5;88m\nContact lookup failed \033[0;0m')
			elif contacts_choice == 5:
				if contacts.modify_contact() is True:
					print('\033[38;5;118m\nContact modified successfully \033[0;0m')
				else:
					print('\033[48;5;88m\nUnable to modify contact!\033[0;0m')
			elif contacts_choice == 6:
				if contacts.import_csv() is True:
					print('\033[38;5;118m\nCSV import successful \033[0;0m')
				else:
					print('\033[48;5;88m\nCSV import failed!\033[0;0m')
			elif contacts_choice == 7:
				if contacts.export_csv() is True:
					print('\033[38;5;118m\nCSV export successful \033[0;0m')
				else:
					print('\033[48;5;88m\nCSV export failed!\033[0;0m')
			elif contacts_choice == 8:
				_user_management()
				helper.clear_screen()
			else:
				helper.trigger_exit()
	except EOFError:
		_contacts_management()
	except ValueError:
		print('\033[48;5;88m\nError: Invalid Input. Please try again!\033[0;0m')
		_contacts_management()


if __name__ == "__main__":
	try:
		helper.clear_screen()
		_user_management()
		helper.clear_screen()
	except KeyboardInterrupt:
		helper.trigger_exit()

	try:
		_contacts_management()
		helper.clear_screen()
	except KeyboardInterrupt:
		helper.trigger_exit()
