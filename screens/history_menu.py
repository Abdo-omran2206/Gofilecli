from rich.console import Console
from rich.table import Table
from utils.ui import clear, copy_link, format_size
from art import *
from utils.ui import Colors
from time import sleep

class History:
    def __init__(self,db):
        self.db = db
        self.history = db.get_history()

    def show(self):
        self.render_header()
        self.table_view()
        number = input("\nEnter the Id of the file to view details or 'b' to go back: ")
        if number.lower() == 'b':
            return
        else:
            clear()
            self.view_details(number)

    def render_header(self):
        clear()
        if not self.history:
            print("No upload history found.")
            input("Press Enter to return to the main menu...")
            return
        print(f"{Colors.Cy}")
        tprint("Upload History")
        print(f"{Colors.Gr}")

    def table_view(self):
        console = Console()
        table = Table()
        table.title = "Upload History"
        table.add_column("Id", style="cyan", justify="center")
        table.add_column("File Name", style="green", justify="center")
        table.add_column("Upload Date", style="yellow", justify="center")
        for x in self.history:
            table.add_row(str(x[0]), str(x[1]), str(x[2]))
        
        console.print(table)
    
    def view_details(self,number):
        data = self.db.get_history_of_file(number)
        if not data:
            print("No details found for the selected file.")
            input("Press Enter to return to the history menu...")
            self.show()
        for x in data:
            if str(x[0]) == number:
                print(f"{Colors.Cy}")
                tprint(f"File Details")
                print(f"{Colors.Gr}")
                console = Console()
                details_table = Table(title="File Details")
                details_table.add_column("Property", style="cyan")
                details_table.add_column("Value", style="green")
                details_table.add_row("File ID", str(x[0]))
                details_table.add_row("File Name", str(x[1]))
                details_table.add_row("Original Path", str(x[2]))
                details_table.add_row("Folder ID", str(x[3]))
                details_table.add_row("Download Link", str(x[4]))
                details_table.add_row("Size", format_size(x[5]))
                details_table.add_row("File Type", str(x[6]))
                details_table.add_row("Created at", str(x[7]))
                console.print(details_table)
                print(f"\n{Colors.Wh}1. Copy Download Link")
                print(f"{Colors.Wh}2. Delete from History")
                print(f"{Colors.Wh}3. Back to History")
                print(f"{Colors.Wh}4. Back to Main Menu")
                selector = input(f"\n{Colors.Wh}==> ")
                self.handle_selection(selector, x, number)

    def handle_selection(self, selector, x, number):
        if selector == "1":
            copy_link(x[4])
            print("Download link copied to clipboard.")
            sleep(2)
            self.show()
        elif selector == "2":
            self.db.delete_file_from_history(number)
            print("File deleted from history.")
            sleep(1)
            self.show()
        elif selector == "3":
            self.show()
        else:
            return