import json
import os

class Config:
    def __init__(self):
        self.config_dir = 'config'
        self.config_path = os.path.join(self.config_dir, 'config.json')
        self._data = {}
        self._ensure_config_exists()
        self._load()

    def _ensure_config_exists(self):
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir, exist_ok=True)
        if not os.path.exists(self.config_path):
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump({"Account_status": "guest"}, f, indent=4)

    def _load(self):
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            self._data = {"Account_status": "guest"}
            self._save()

    def _save(self):
        with open(self.config_path, 'w', encoding='utf-8') as f:
            json.dump(self._data, f, indent=4)

    def get_token(self):
        status = self._data.get("Account_status", "guest")
        if status != "active":
            return None
        return self._data.get("UserToken")
    
    def add_token(self, token):
        self._data["UserToken"] = token
        self._data["Account_status"] = "active"
        self._save()
        return True

    def remove_token(self):
        self._data.pop("UserToken", None)
        self._data["Account_status"] = "guest"
        self._save()
        return True
    
    def set_account_status(self):
        status = self._data.get("Account_status", "guest")
        self._data["Account_status"] = "active" if status != "active" else "guest"
        self._save()
        return True
    
    def get_account_status(self):
        return self._data.get("Account_status", "guest")