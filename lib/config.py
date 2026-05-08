import json
import os

class Config:
    def __init__(self):
        if not os.path.exists('config'):
            os.makedirs('config', exist_ok=True)
        if not os.path.exists('config/config.json'):
            with open('config/config.json', 'w') as f:
                f.write('{"Account_status":"guest"}')
    
    def get_token(self):
        with open('config/config.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return None
        token = data.get("UserToken", None)
        return token
    
    def add_token(self, token):
        with open('config/config.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        data["UserToken"] = token
        data["Account_status"] = "active"
        with open('config/config.json', 'w') as f:
            json.dump(data, f, indent=4)
            return True
        return False

    def remove_token(self):
        with open('config/config.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        data.pop("UserToken", None)
        data["Account_status"] = "guest"
        with open('config/config.json', 'w') as f:
            json.dump(data, f, indent=4)
            return True
        return False
    
    def set_account_status(self):
        with open('config/config.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        status = data["Account_status"]
        if status == "active":
            data["Account_status"] = "guest"
        else:
            data["Account_status"] = "active"
        with open('config/config.json', 'w') as f:
            json.dump(data, f, indent=4)
            return True
        return False
    
    def get_account_status(self):
        with open('config/config.json', 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return None
        account_status = data.get("Account_status", None)
        return account_status