import os
from datetime import datetime

class Log:
    def __init__(self, path: str) -> None:
        self.path = path

    def write(self, id: int, file: str, job: str = "observer") -> None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        __output = f"{date} {job}[{id}]: {file} changed!\n"
        with open(self.path, "a") as f:
            f.write(__output)
            f.close()