import requests
import os

class Gofile:
    def __init__(self, token=None):
        self.token = token
        self.api_base = "https://api.gofile.io"

    def checkApi(self):
        try:
            checkApi_response = requests.get(
                url=self.api_base
            ).json()
            if checkApi_response["status"] == 'ok':
                return True
        except Exception:
            pass
        return False

    def _get_best_server(self):
        response = requests.get(f"{self.api_base}/servers")
        data = response.json()
        if data["status"] == "ok":
            return data["data"]["servers"][0]["name"]
        raise Exception("Could not retrieve an available server.")    
    
    def response_handler(self, response):
        try:
            res_json = response.json()
            if res_json.get("status") == "ok":
                return res_json.get("data")
            return res_json # Returns error details if status isn't 'ok'
        except Exception:
            return {"error": "Invalid JSON response", "status_code": response.status_code}

    def upload_file(self, file_path,Folder_Path=None):

        server = self._get_best_server()
        url = f"https://{server}.gofile.io/uploadfile"
        
        # Prepare data and files
        payload = {"token": self.token ,"folderId": Folder_Path} if self.token else {}
        if not os.path.exists(file_path):
            print("File not found")
            return
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, data=payload, files=files)          
        return self.response_handler(response)
    
    def upload_folder(self, folder_path):

        if not os.path.isdir(folder_path):
            print("Folder not found")
            return
        
        files = []
        
        for root, _, filenames in os.walk(folder_path):
            for filename in filenames:
                files.append(os.path.join(root, filename))

        if not files:
            print("No files found")
            return
        
        results = []

        first_upload = self.upload_file(files[0])
        results.append(first_upload)
        
        try:
            folder_id = first_upload["parentFolder"]
        except:
            print("Failed to get folderId")
            return results

        for file in files[1:]:
            res = self.upload_file(file, Folder_Path=folder_id)
            results.append(res)
            
        return results
