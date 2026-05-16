from cli.parser import create_parser
from lib.db import Database
from lib.config import Config
from utils.ui import Colors
from screens.account_menu import AccountMenu
from screens.settings_menu import Settings
from screens.upload_menu import UploadFile
from screens.history_menu import History
from art import tprint
import os
from time import sleep

# 1. Setup
Config()
db = Database()
db.initDataBase()


def GUI():
    os.system('cls' if os.name == 'nt' else 'clear')
    options = ["Upload File", "View History", "Account","Settings","Exit"]
    print(Colors.Cy)
    tprint("Gofile", font="slant")
    for i, option in enumerate(options, 1):
        print(f"{Colors.Wh}{i}. {option}")

def main():
    try:
        while True:
            GUI()
            selector = input("\nSelect an option: ")
            print()
            if selector == "1":
                UploadFile(db).show()
            elif selector == "2":
                History(db).show()
            elif selector == "3":
                AccountMenu(db).show()
            elif selector == "4":
                Settings(db).show()
            elif selector == "5":
                print(f"{Colors.Re}Exiting the program. Goodbye!")
                break
            else:
                print(f"{Colors.Re}Invalid option. Please select a valid number from the menu.")
                sleep(2)
    except KeyboardInterrupt:
        print(f"\n{Colors.Re}Interrupted by user. Exiting...")
    finally:
        db.close()

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        GUI()
        main()