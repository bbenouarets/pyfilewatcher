import os
import sys
import time
import threading
import hashlib
import difflib
from datetime import datetime

class Watcher(threading.Thread):
    def __init__(self, path: str = None, interval: int = 1, callback: callable = None, output: bool = False) -> None:
        super().__init__()
        self.interval = interval
        if path is None:
            sys.exit("❌ Path is not specified.")
        else:
            self.path = path
        self.__output = output
        if callback is None:
            self._callback = print
        else:
            self._callback = callback

    def change(self, content: str) -> list:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_content = self.read()
        differ = difflib.Differ()
        diff = list(differ.compare(content.splitlines(), new_content.splitlines()))
        for d in diff:
            status = d[0]
            if status == "-":
                value = d[2:]
                text = f"{date} - [{status}] {self.path}: {value}"
                self._callback(text, str(value))
            elif status == "+":
                value = d[2:]
                text = f"{date} - [{status}] {self.path}: {value}"
                self._callback(text, str(value))
            else:
                continue
        return new_content

    def read(self) -> str:
        with open(self.path, "r") as f:
            data = f.read()
        return data

    def hash(self) -> str:
        with open(self.path, "rb") as f:
            text = f.read()
        return hashlib.sha256(text).hexdigest()

    def compare(self, hash: str) -> tuple:
        h = self.hash()
        if hash == h:
            return (h, False)
        else:
            return (h, True)

    def monitor(self) -> None:
        content = self.read()
        hash = self.hash()
        modified = os.stat(self.path).st_mtime
        while True:
            m = os.stat(self.path).st_mtime
            if m != modified:
                modified = m
                new_hash, change = self.compare(hash)
                if change:
                    hash = new_hash
                    new = self.change(content=content)
                    content = new
            time.sleep(self.interval)

    def run(self) -> None:
        self.monitor()