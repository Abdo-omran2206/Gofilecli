import os
from dotenv import load_dotenv , set_key
from pathlib import Path
class Config:
    def __init__(self):
        load_dotenv()
        self.env_path = Path('.env')
        if not self.env_path.exists():
            self.env_path.touch()

    def get_token(self):
        return os.getenv("API_TOKEN")
    
    def get_account_status(self):
        return os.getenv("ACCOUNT_STATUS", 'guest')

    def add_token(self, token):
        if not token:
            raise ValueError("Token cannot be empty")
        if self.env_path.exists():
            set_key(self.env_path, 'API_TOKEN', token)
            set_key(self.env_path, 'ACCOUNT_STATUS', 'active')
        return True
    
    def remove_token(self):
        if self.env_path.exists():
            set_key(self.env_path, 'API_TOKEN', '')
            set_key(self.env_path, 'ACCOUNT_STATUS', 'guest')
        return True
    
    def set_account_status(self):
        if self.env_path.exists():
            status = self.get_account_status()            
            new_status = 'guest' if status == 'active' else 'active'
            set_key(self.env_path, 'ACCOUNT_STATUS', new_status)
        return True 