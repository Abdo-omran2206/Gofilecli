from lib.Gofile import Gofile
from lib.config import Config
from utils.ui import Colors , clear , copy_link
from art import tprint
from time import sleep

class UploadFile:
    def __init__(self , db):
        self.db = db
        self.config = Config()
        Token = self.config.get_token()
        self.gofile_client = Gofile(token=Token) # Pass your token here if you have one

    def show(self):
        
        if not self.api_check():
            return

        self.render_header()
        
        path = input(f"\n{Colors.Wh}Enter the path of file ==> ")

        if path == "":
            return
        
        print(f"\n{Colors.Gr}Uploading file...")
        data = self.gofile_client.upload_file(path)
        
        status_of_save_data_db = self.save_uploaded_data_to_db(data,path)

        if status_of_save_data_db:
            print(f"{Colors.Gr}File uploaded and data saved to database successfully.")
        else:
            print(f"{Colors.Re}File uploaded but failed to save data to database.")

        print(f"\n{Colors.Gr}File Name: {data['name']}")
        print(f"{Colors.Gr}Download Link: {data['downloadPage']}\n")
        
        self.show_download_options(data)

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
        
class UploadFolder:
    def __init__(self , db):
        self.db = db
        self.config = Config()
        self.Token = self.config.get_token()
        self.gofile_client = Gofile(token=self.Token) # Pass your token here if you have one

    def render_header(self):
        clear()
        print(Colors.Gr)
        tprint("Upload Folder")
        print(f"{Colors.Ye}Note: Make sure to provide the correct folder path. Example: C:\\Users\\Username\\Documents\\folder")
        print(f"{Colors.Ye}to back to main menu, just press Enter without typing anything.")

        print(f"{Colors.Ye}\nAccount Status: {Colors.Wh}{self.config.get_account_status()}")

    def show(self):
        
        self.render_header()
        if not self.Token:
            print(f"{Colors.Ye}\nNo token found. Uploading without a token may have limitations.")
            sleep(2)
            return
        
        if not self.api_check():
            return

        path = input(f"\n{Colors.Wh}Enter the path of folder ==> ")

        if path == "":
            return
        
        print(f"\n{Colors.Gr}Uploading folder...")
        data = self.gofile_client.upload_folder(path)

        returned_data = []
        for file_data in data:
            status = self.save_uploaded_data_to_db(file_data,path)
            returned_data.append(status)
        
        if all(returned_data):
            print(f"{Colors.Gr}File uploaded and data saved to database successfully.")
        else:
            print(f"{Colors.Re}File uploaded but failed to save data to database.")

        print(f"\n{Colors.Gr}Directory Name: {data[0]['parentFolderCode']}")
        print(f"{Colors.Gr}Download Link: {data[0]['downloadPage']}\n")
        
        self.show_download_options(data[0])
        
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