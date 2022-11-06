"""phonebook is a simple contact management tool written in python."""

from utils import helper as h
from utils import user as u
from utils.contacts import _set_tablename
from utils.helper import MenuUser as MU
from utils.management_contact import cont_maper
# from utils.management_user import _user_management
# from utils.management_contact import _contacts_management
from utils.management_contact import cont_maper
from utils.prints import menu_text_user, menu_text_contacts, UserFailed as UF, UserSuccessfully as US


def _input_user_menu_choice():
	"""Displays user management options and returns user's input choice"""
	print('~' * 20, '\n\033[38;5;63mUser Management Menu\033[0;0m\n' + '~' * 20, menu_text_user)

	choice = int(input('Input choice: '))
	h.clear_screen()
	if choice < 0 or choice > 3:
		raise ValueError
	return choice


def _input_contact_menu_choice():
	"""Displays contact management options and returns user's input choice"""
	choice = 0

	print('~' * 23, '\n\033[38;5;63mContact Management Menu\033[0;0m\n' + '~' * 23, menu_text_contacts)

	choice = int(input('Input choice: '))
	h.clear_screen()
	if choice < 1 or choice > 9:
		raise ValueError
	return choice


def _user_management():
	"""Processes user management menu input"""
	# Redraw user management menu until a user is successfully selected
	try:
		while True:
			user_choice = _input_user_menu_choice()
			# user_maper[user_choice]()

			if user_choice == MU.ADD_USER.value:
				if u.add_user():
					US.succ_add_user(None)
				else:
					UF.err_add(None)

			elif user_choice == MU.DELETE_USER.value:
				if u.remove_user():
					US.succ_remove_user(None)
				else:
					UF.err_rem(None)

			elif user_choice == MU.SELECT_USER.value:
				if u.select_user():
					US.succ_select_user(None)
					break
				else:
					UF.err_select(None)
			else:
				h.trigger_exit()

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

			cont_maper[contacts_choice]()

	except EOFError:
		_contacts_management()
	except ValueError:
		print('\033[48;5;88m\nError: Invalid Input. Please try again!\033[0;0m')
		_contacts_management()


if __name__ == "__main__":
	try:
		h.clear_screen()
		_user_management()
		h.clear_screen()
	except KeyboardInterrupt:
		h.trigger_exit()

	try:
		_contacts_management()
		h.clear_screen()
	except KeyboardInterrupt:
		h.trigger_exit()
