import os
import sys
import time
import hashlib
import threading

class Watcher(threading.Thread):
    def __init__(self, name: str = "HOME", file: str = None) -> None:
        threading.Thread.__init__(self)
        self.file = file
        self.name = name

    def hash(self) -> str:
        try:
            with open(self.file, "rb") as f:
                CONTENT = f.read()
            return hashlib.sha256(CONTENT).hexdigest()
        except FileNotFoundError:
            sys.exit(f"[{self.name}] File deleted! {self.file}")

    def content(self) -> str:
        try:
            with open(self.file, "r") as f:
                CONTENT = f.read()
            return CONTENT
        except FileNotFoundError:
            sys.exit(f"[{self.name}] File deleted! {self.file}")

    def run(self) -> None:
        try:
            LAST_MODIFIED = os.stat(self.file).st_mtime
        except FileNotFoundError:
            print(f"[{self.name}] File not exist! {self.file}")
            sys.exit(1)
        OLD_HASH = self.hash()
        OLD_CONTENT = self.content()
        while True:
            try:
                CURRENT_MODIFIED = os.stat(self.file).st_mtime
            except FileNotFoundError:
                sys.exit(f"[{self.name}] File deleted! {self.file}")
            if CURRENT_MODIFIED > LAST_MODIFIED:
                NEW_HASH = self.hash()
                NEW_CONTENT = self.content()
                if NEW_HASH != OLD_HASH:
                    print(f"[{self.name}] Change in {self.file}!")
                    OLD_HASH = NEW_HASH
                    OLD_CONTENT = NEW_CONTENT
                LAST_MODIFIED = CURRENT_MODIFIED
            time.sleep(1)
            
    def start(self) -> None:
        threading.Thread.start(self)

class FileWatcher():
    def __init__(self, name: str = None, files: list = None, interval: int = 1) -> None:
        self.FILES = files
        self.INTERVAL = interval
        self.THREADS = []
        self.NAME = name
    
    def __call__(self) -> None:
        for file in self.FILES:
            t = Watcher(name=self.NAME, file=file)
            self.THREADS.append(t)
            t.start()