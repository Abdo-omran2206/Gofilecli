import os
import pyperclip
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, TransferSpeedColumn, DownloadColumn
from contextlib import contextmanager
import time
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

class ProgressFile:
    def __init__(self, file_obj, progress, task, total_size):
        self._file = file_obj
        self._progress = progress
        self._task = task
        self._total_size = total_size
        self._chunk_size = 8192

    def __len__(self):
        return self._total_size

    def read(self, size=-1):
        chunk = self._file.read(size)
        if chunk:
            self._progress.update(self._task, advance=len(chunk))
        return chunk

    def __getattr__(self, name):
        return getattr(self._file, name)

    def __iter__(self):
        return self

    def __next__(self):
        chunk = self.read(self._chunk_size)
        if not chunk:
            raise StopIteration
        return chunk

    def close(self):
        return self._file.close()

@contextmanager
def upload_progress_bar(file_obj, file_name, total_size):
    with Progress(
        TextColumn("[bold blue]Uploading[/] {task.fields[file_name]}"),
        BarColumn(bar_width=None),
        "[progress.percentage]{task.percentage:>3.0f}%",
        "•",
        DownloadColumn(),
        "•",
        TransferSpeedColumn(),
        "•",
        TimeRemainingColumn(),
    ) as progress:

        task = progress.add_task(
            "upload",
            total=total_size,
            file_name=file_name
        )

        yield ProgressFile(file_obj, progress, task, total_size)