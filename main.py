from lib.db import Database
from lib.config import Config
from utils.ui import Colors
from screens.account_menu import AccountMenu
from screens.settings_menu import Settings
from screens.upload_menu import UploadFile
from screens.history_menu import History
from art import *
import os

# 1. Setup
Config()
db = Database()
db.initDataBase()

def GUI():
    os.system('cls' if os.name == 'nt' else 'clear')
    options = ["Upload File", "View History", "Account","Settings","Exit"]
    print(Colors.Cy)
    tprint("Gofile")
    for i, option in enumerate(options, 1):
        print(f"{Colors.Wh}{i}. {option}")

isExit = False
while not isExit:
    GUI()
    selector = input("\nSelect an option: ")
    print()
    if selector == "1":
        uploadFile = UploadFile(db)
        uploadFile.show()
    elif selector == "2":
        history = History(db)
        history.show()
    elif selector == "3":
        AccountMenu(db)
    elif selector == "4":
        Settings(db)
    elif selector == "5":
        print(f"{Colors.Re}Exiting the program. Goodbye!")
        isExit = True
        exit()
    else:
        print(f"{Colors.Re}Invalid option. Please select a valid number from the menu.")
