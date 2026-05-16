import os
from dotenv import load_dotenv , set_key
from pathlib import Path
class Config:
    def __init__(self):
        self.env_path = Path('.env')
        if not self.env_path.exists():
            self.env_path.touch()
            set_key(self.env_path,'API_TOKEN','')
            set_key(self.env_path,'ACCOUNT_STATUS','guest')
            set_key(self.env_path,'AUTO_SAVE','true')
            
        load_dotenv()
        
    def get_token(self):
        return os.getenv("API_TOKEN")
    
    def get_account_status(self):
        return os.getenv("ACCOUNT_STATUS", 'guest')
    
    def get_auto_save(self):
        auto_save_value = os.getenv("AUTO_SAVE", 'true').lower()
        return auto_save_value

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
    
    def toggle_auto_save(self):
        if self.env_path.exists():
            auto_save = self.get_auto_save()
            new_auto_save = 'false' if auto_save == 'true' else 'true'
            set_key(self.env_path, 'AUTO_SAVE', new_auto_save)
        return True