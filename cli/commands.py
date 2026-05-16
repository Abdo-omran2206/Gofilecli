from screens.history_menu import History
from lib.db import Database

db = Database()  # Initialize the database connection

def handle_version(args):
    print("GoFile CLI version 1.0")

def handle_history(args):
    History(db).show()

def handle_token(args):
    pass  # You would implement the logic to set the API token here

def handle_upload(args):
    pass  # You would implement the logic to upload a file here