from lib.config import Config
from utils.ui import Colors
from art import tprint
from utils.ui import clear
from time import sleep

class AccountMenu:
    def __init__(self, db):
        self.db = db
        self.config = Config()

    def show(self):
        clear()
        print(Colors.Ye)
        tprint("Account Menu")

        if self.config.get_account_status() == "active" and self.config.get_token() is not None:
            print(f"{Colors.Gr}Status: Logged In\n")
            print(f"{Colors.Re}1. Logout")
            print(f"{Colors.Gr}2. Back to Main Menu")
            selector = input(f"{Colors.Ye}\n==> ")
            if selector == "1":
                is_removed = self.config.remove_token()
                if is_removed:
                    print(f"{Colors.Gr}Logged out successfully!")
                else:
                    print(f"{Colors.Re}Failed to log out.")
                sleep(1)
            else:
                print(f"{Colors.Ye}Returning to Main Menu...")
                sleep(1)
        else:
            print(f"{Colors.Re}Status: Guest\n")
            print(f"{Colors.Gr}1. Login")
            print(f"{Colors.Re}2. Back to Main Menu")
            select = input(f"{Colors.Ye}\n==> ")
            if select == "1":
                token = input("Enter your token: ")
                is_added = self.config.add_token(token)
                if is_added:
                    print(f"{Colors.Gr}Token added successfully!")
                else:
                    print(f"{Colors.Re}Failed to add token.")
                sleep(1)
            else:
                print(f"{Colors.Ye}Returning to Main Menu...")
                sleep(1)
