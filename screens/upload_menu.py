from lib.Gofile import Gofile
from lib.config import Config
from utils.ui import Colors , clear , copy_link
from art import tprint
from time import sleep
import os

class UploadFile:
    def __init__(self , db):
        self.db = db
        self.config = Config()
        self.Token = self.config.get_token()
        self.auto_save = self.config.get_auto_save()
        self.gofile_client = Gofile(token=self.Token) # Pass your token here if you have one

    def show(self):
        
        if not self.api_check():
            print(f"{Colors.Re}Cannot proceed with file upload without API access.")
            input(f"{Colors.Ye}Press Enter to return to main menu...")
            return

        self.render_header()
        
        path = input(f"\n{Colors.Wh}Enter the path of file ==> ")

        if path.strip() == "":
            print(f"{Colors.Ye}Returning to main menu...")
            sleep(2)
            return

        path_check_result = self.Check_path(path)

        if path_check_result is None:
            print(f"{Colors.Re}Invalid path. Please provide a valid file or directory path.")
            input(f"{Colors.Ye}Press Enter to return to main menu...")
            return
        
        status_of_save_data_db = False
        
        if path_check_result == "file":
            data = self.gofile_client.upload_file(path)
            if self.auto_save.lower() == 'true':
                print(self.auto_save)
                status_of_save_data_db = self.save_uploaded_data_core(data,path,"file")
            
        elif path_check_result == "directory":
            if self.Token is not None and self.config.get_account_status() == "active":
                data = self.gofile_client.upload_folder(path)
                if self.auto_save.lower() == 'true':
                    status_of_save_data_db = self.save_uploaded_data_core(data,path,"directory")
            else:
                print(f"{Colors.Re}Directory upload is only available for active accounts. Please check your account status or upload a file instead.")
                input(f"{Colors.Ye}Press Enter to return to main menu...")
                return
        else:
            print(f"{Colors.Re}Unexpected error occurred while checking the path.")
            input(f"{Colors.Ye}Press Enter to return to main menu...")
            return

        if status_of_save_data_db and self.auto_save.lower() == 'true':
            print(self.auto_save)
            print(f"{Colors.Gr}File uploaded and data saved to database successfully.")
        else:
            print(f"{Colors.Re}File uploaded successfully")

        if path_check_result == "directory":
            print(f"\n{Colors.Gr}Directory Name: {data[0]['name']}")
            print(f"{Colors.Gr}Download Link: {data[0]['downloadPage']}\n")
        else:
            print(f"\n{Colors.Gr}File Name: {data['name']}")
            print(f"{Colors.Gr}Download Link: {data['downloadPage']}\n")
        self.show_download_options(data)


    def save_uploaded_data_core(self,data,path,upload_type):
        if upload_type == "file":
            return self.save_uploaded_data_to_db(data,path)
        elif upload_type == "directory":
            returned_data = []
            for file_data in data:
                status = self.save_uploaded_data_to_db(file_data,path)
                returned_data.append(status)
            return all(returned_data)
        else:
            return False

    def Check_path(self,path):
        if os.path.isfile(path):
            return "file"

        if os.path.isdir(path):
            return "directory"
        
        return None

    def render_header(self):
        clear()
        print(Colors.Gr)
        tprint("Upload File")
        print(f"{Colors.Ye}Note: Make sure to provide the correct file path. Example: C:\\Users\\Username\\Documents\\file.txt")
        print(f"{Colors.Ye}to back to main menu, just press Enter without typing anything.")

        print(f"{Colors.Ye}\nAccount Status: {Colors.Wh}{self.config.get_account_status()}")

    def save_uploaded_data_to_db(self,data,path):
        if data and "downloadPage" in data:
            self.db.insert_file(
                download_link=data["downloadPage"], 
                orginal_path=path, 
                gofile_id=data["parentFolder"], # Gofile uses 'parentFolder' for the ID
                file_name=data["name"], 
                file_type=data.get("mimetype", "unknown"), # Use .get() to avoid KeyErrors
                size=data["size"]
            )
            return True
        else:
            return False

    def api_check(self):
        checkApi = self.gofile_client.checkApi()
        if not checkApi:
            print(f"{Colors.Re}Gofile API is not reachable.")
            input(f"{Colors.Ye}Press Enter to return to main menu...")
            return
        return True
    
    def show_download_options(self, data):
        options = ["Copy Download Link" , "Back to Main Menu"]
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        selector = input("\n==> ")

        if selector == "1":
            copy_link(data['downloadPage'])
            print(f"{Colors.Ye}Download link copied to clipboard.")
            sleep(2)
            return
        else:
            return