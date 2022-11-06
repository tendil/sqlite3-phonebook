class ContactSuccessfully:
	def contact_add(self):
		print('\033[38;5;118m\nContact added successfully\n\033[0;0m')

	def contact_del(self):
		print('\033[38;5;118m\nContact deleted successfully\n\033[0;0m')

	def contact_modify(self):
		print('\033[38;5;118m\nContact modified successfully\n\033[0;0m')

	def contact_import(self):
		print('\033[38;5;118m\nCSV import successful\n\033[0;0m')

	def contact_export(self):
		print('\033[38;5;118m\nCSV export successful\n\033[0;0m')


class PrintFailed:
	def not_add_cont(self):
		print('\033[48;5;88m\nCould not add contact!\n\033[0;0m')

	def not_cont_del(self):
		print('\033[48;5;88m\nContact not found!\n\033[0;0m')

	def not_shear_cont(self):
		print('\033[48;5;88m\nContact lookup failed\n\033[0;0m')

	def not_modify_cont(self):
		print('\033[48;5;88m\nUnable to modify contact!\n\033[0;0m')

	def not_imoprt_cont(self):
		print('\033[48;5;88m\nCSV import failed!\n\033[0;0m')

	def not_export_cont(self):
		print('\033[48;5;88m\nCSV export failed!\n\033[0;0m')


class UserSuccessfully:
	def succ_add_user(self):
		print('\033[38;5;118m\nUser successfully added \033[0;0m\n')

	def succ_remove_user(self):
		print('\033[38;5;118m\nUser successfully removed \033[0;0m\n')

	def succ_select_user(self):
		print('\033[38;5;118m\nUser successfully selected \033[0;0m\n')


class UserFailed:
	def err_add(self):
		print('\033[48;5;88m\nError: user already exists \033[0;0m\n')

	def err_rem(self):
		print('\033[48;5;88m\nError: user does not exist \033[0;0m\n')

	def err_select(self):
		print('\033[48;5;88m\nError: user does not exist \033[0;0m\n')


menu_text_contacts = """

1. Show all contacts
2. Add contact
3. Delete contact
4. Search contact
5. Modify contact
6. Import CSV
7. Export CSV
8. Switch to user management mode
9. Exit
		"""

menu_text_user = """

1. Add user
2. Delete user
3. Select user
0. Exit
	"""

