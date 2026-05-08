from lib.config import Config
from utils.ui import Colors
from art import tprint
from utils.ui import clear
from time import sleep
class Settings:
    def __init__(self,db):
        self.db = db
        self.config = Config()
        self.display_menu()

    def display_menu(self):
        clear()
        print(Colors.Cy)
        tprint("Settings Menu")

        print(f"\n{Colors.Wh}1. Change Account Status")
        print(f"{Colors.Wh}2. Toggle Auto Save History (on/off)")
        print(f"{Colors.Wh}3. Clear History")
        print(f"{Colors.Wh}4. Back to Main Menu")
    
        selector = input(f"\n{Colors.Wh}==> ")

        self.handle_selection(selector)

    def handle_selection(self, selector):
        if selector == "1":
            status = self.config.set_account_status()
            if status:
                print(f"{Colors.Gr}Account status changed successfully!")
            else:
                print(f"{Colors.Re}Failed to change account status.")
            sleep(2)
            return
        elif selector == "2":
            print(f"{Colors.Ye}Comming soon...")
            sleep(1)
            return
        elif selector == "3":
            print(f"{Colors.Wh}Clearing history...")
            result =  self.db.clear_history()
            if result:
                print(f"{Colors.Gr}History cleared successfully!")
            else:
                print(f"{Colors.Re}Failed to clear history.")
            sleep(2)
            return
        elif selector == "4":
            print(f"{Colors.Ye}Returning to Main Menu...")
            sleep(2)
            return
        else:
            print(f"{Colors.Re}Invalid selection. Please try again.")