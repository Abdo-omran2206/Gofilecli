from lib.config import Config
from utils.ui import Colors
from art import tprint
from utils.ui import clear
from time import sleep
class AccountMenu:
    def __init__(self, db):
        self.db = db
        self.config = Config()
        self.display_menu()
        # self.handle_selection(selector)

    def display_menu(self):
        clear()
        print(Colors.Ye)
        tprint("Account Menu")
        if self.config.get_account_status() == "active" and self.config.get_token() is not None:
            print(f"{Colors.Gr}Status: Logged In\n")
            print(f"{Colors.Re}1. Logout")
            print(f"{Colors.Gr}2. Back to Main Menu")
            selector = input(f"{Colors.Ye}\n==> ")
            if selector == "1":
                isRemoved = self.config.remove_token()
                if isRemoved:
                    print(f"{Colors.Gr}Logged out successfully!")
                    sleep(1)
                else:
                    print(f"{Colors.Re}Failed to log out.")
                    sleep(1)
            else:
                print(f"{Colors.Ye}Returning to Main Menu...")
                sleep(1)
                return
        else:
            print(f"{Colors.Re}Status: Guest\n")
            print(f"{Colors.Gr}1. Login")
            print(f"{Colors.Re}2. Back to Main Menu")
            select = input(f"{Colors.Ye}\n==> ")
            if select == "1":
                token = input("Enter your token: ")
                isAdded = self.config.add_token(token)
                if isAdded:
                    print(f"{Colors.Gr}Token added successfully!")
                    sleep(1)
                else:
                    print(f"{Colors.Re}Failed to add token.")
                    sleep(1)
            else:
                print(f"{Colors.Ye}Returning to Main Menu...")
                sleep(1)
                return