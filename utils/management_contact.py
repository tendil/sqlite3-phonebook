#from phonebook import _user_management
from utils.helper import MenuContacts, trigger_exit
from utils.prints import PrintFailed as PF, ContactSuccessfully as CS
from utils import contacts as c


cont_maper = {
	MenuContacts.ALL_CONTACTS.value: lambda: c.show_all_contacts(),
	MenuContacts.ADD_CONTACT.value: lambda: CS.contact_add(None) if c.add_contact() else PF.not_add_cont(None),
	MenuContacts.DELETE_CONTACT.value: lambda: CS.contact_del(None) if c.delete_contact() else PF.not_cont_del(None),
	MenuContacts.SEARCH_CONTACT.value: lambda: PF.not_shear_cont(None) if c.search_contact() is False else None,
	MenuContacts.MODIFY_CONTACT.value: lambda: CS.contact_modify(None) if c.modify_contact() else PF.not_modify_cont(None),
	MenuContacts.IMPORT_CSV.value: lambda: CS.contact_import(None) if c.import_csv() else PF.not_imoprt_cont(None),
	MenuContacts.EXPORT_CSV.value: lambda: CS.contact_export(None) if c.export_csv() else PF.not_export_cont(None),
	#MenuContacts.USER_MANAGEMENT.value: lambda: _user_management(),
	MenuContacts.EXIT.value:lambda: trigger_exit()
}

