> A simple python CLI app for managing phonebooks for various users. In it, you can save the contacts of your friends to 
> always be in touch. This is my little project. Its development is underway and it is not finished yet. I have not yet 
> come up with a decent name for it.

- Seperate contact list maintained for each user
- Powered by a integer input based command line menu interface.  
- The persistance is handled by an sqlite3 database, material.db.
- User credentials are encrypted.

## IMAGE'S

<details>
<summary>
Image's of this project 📈
</summary>
<img src="https://github.com/tendil/sqlite3-phonebook/blob/main/static/user_menu.png" height="400" width="400">
<img src="https://github.com/tendil/sqlite3-phonebook/blob/main/static/add_user.png" height="400" width="400">
<img src="https://github.com/tendil/sqlite3-phonebook/blob/main/static/contact_menu.png" height="400" width="400">
<img src="https://github.com/tendil/sqlite3-phonebook/blob/main/static/show_all_contacts.png" height="400" width="400">
<img src="https://github.com/tendil/sqlite3-phonebook/blob/main/static/export.png" height="400" width="800">
</details>


## License

[MIT License](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)

## Authors

* <a href="https://github.com/tendil">Me</a>
* Some people with telegram chats 

## What I plan to add to this project:
-  Added hotkeys so that you can return to the main menu if you make a wrong choice.
- Improve the output interface (make a highlight, and when adding / changing / deleting a contact, display its name).
- Make a function to display all users. 
- Make the function of deleting the database, with confirmation, entering the user's password.

## Features:
#### User Management:
- Add User
- Delete User
- Select user

#### Contact Management:
- Show All Contacts
- Add Contact (name and number mandatory, email optional)
- Delete Contact (Select on basis of name, case insensitive)
- Search Contact (Select on basis of name, case insensitive)
- Modify Contact (Select on basis of name, case insensitive)
- Import CSV (In format: name, contact, email)
- Export CSV (In format: name, contact, email)

## Usage

#### **Clone or download this repository**

```python
git clone 
```

#### We go to the terminal and go to the directory with the repository:

```python
cd sqlite3_phonebook
```

```python
python3 -m venv venv
```

```python
source venv/bin/activate
 ```

```python
pip install -r requirements.txt
```

```python
python3 phonebook.py
```

## Support

### For support, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)

## Feedback

### If you have any feedback, telegram [@XllrepoDewelloper](https://t.me/XllrepoDewelloper)

## Contributing

### Contributions are always welcome!

