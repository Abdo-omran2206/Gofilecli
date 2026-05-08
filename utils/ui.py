import os
import pyperclip

class Colors:
    Bl = '\033[30m'  # Colors foormatting output
    Re = '\033[1;31m'
    Gr = '\033[1;32m'
    Ye = '\033[1;33m'
    Blu = '\033[1;34m'
    Mage = '\033[1;35m'
    Cy = '\033[1;36m'
    Wh = '\033[1;37m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def copy_link(link):
    pyperclip.copy(link)

def format_size(size):
    for unit in ['B','KB','MB','GB']:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024