import sqlite3
import os

class Database:
    def __init__(self):
        if not os.path.exists('data'):
            os.makedirs('data', exist_ok=True)
            
        self.conn = sqlite3.connect('data/gofilecli.db')
        self.cursor = self.conn.cursor()
        
    def initDataBase(self):
        
        try:
            self.conn.execute('''
CREATE TABLE IF NOT EXISTS files (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             file_name TEXT NOT NULL,
             orginal_path TEXT NOT NULL,
             gofile_id TEXT NOT NULL,
             download_link TEXT NOT NULL,
             size INTEGER NOT NULL,
             file_type TEXT NOT NULL,
             created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
             )
            ''')
            self.conn.commit()
        except Exception as e:
            print(f"Database initialization error: {e}")

    def insert_file(self, file_name, orginal_path, gofile_id, download_link, size, file_type):
        self.cursor.execute('''
            INSERT INTO files (file_name, orginal_path, gofile_id, download_link, size, file_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (file_name, orginal_path, gofile_id, download_link, size, file_type))
        self.conn.commit()

    def get_folders_id(self):
        try:
            # Create a cursor from the connection
            cursor = self.conn.cursor()
            cursor.execute('SELECT gofile_id,file_name FROM files')
            
            # Fetch all results
            data = cursor.fetchall()
            return data
        except Exception as e:
            # Print the actual error message, not the class name
            print(f"Database error: {e}")
            return []
    
    def get_history(self):
        try:
            # Create a cursor from the connection
            cursor = self.conn.cursor()
            cursor.execute('SELECT id,file_name,created_at FROM files')
            
            # Fetch all results
            data = cursor.fetchall()
            return data
        except Exception as e:
            # Print the actual error message, not the class name
            print(f"Database error: {e}")
            return []
        
    def get_history_of_file(self, file_id):
        try:
            # Create a cursor from the connection
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM files WHERE id = ?', (file_id,))
            
            # Fetch all results
            data = cursor.fetchall()
            return data
        except Exception as e:
            # Print the actual error message, not the class name
            print(f"Database error: {e}")
            return []
        
    def delete_file_from_history(self, file_id):
        try:
            # Create a cursor from the connection
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM files WHERE id = ?', (file_id,))
            self.conn.commit()
        except Exception as e:
            # Print the actual error message, not the class name
            print(f"Database error: {e}")

    def clear_history(self):
        try:
            # Create a cursor from the connection
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM files')
            self.conn.commit()
            return True
        except Exception as e:
            # Print the actual error message, not the class name
            print(f"Database error: {e}")
            return False