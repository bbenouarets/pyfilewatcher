import os
import time
import threading
import hashlib

class Watcher(threading.Thread):
    def __init__(self, file: str, interval: int, callback: callable) -> None:
        super().__init__()
        self.__file = file
        self.__interval = interval
        self.__callback = callback

    def __read(self) -> str:
        with open(self.__file, "r") as f:
            return f.read()

    def __props(self) -> str:
        return os.stat(self.__file)

    def __mtime(self) -> str:
        return os.stat(self.__file).st_mtime    

    def __ino(self) -> str:
        return os.stat(self.__file).st_ino

    def __hash(self) -> str:
        with open(self.__file, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def compare(self, value: str, ref: str) -> bool:
        if value != ref:
            return True
        else:
            return False

    def __watch(self) -> None:
        mtime = self.__mtime()
        h = self.__hash()
        while True:
            n_mtime = self.__mtime()
            if mtime != n_mtime:
                n_h = self.__hash()
                if self.compare(h, n_h):
                    self.__callback(self.native_id, self.__file, "observer")
                    h = n_h
                    mtime = n_mtime
                else:
                    mtime = n_mtime
            time.sleep(self.__interval)

    def run(self) -> None:
        self.__watch()