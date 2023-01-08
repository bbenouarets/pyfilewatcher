import os

class LogHandler:
    def __init__(self, path: str) -> None:
        self.path = path

    def write(self, text: str, raw: str, output: bool = False) -> None:
        if output:
            print(f"✎ {raw}")
        with open(self.path, "a") as f:
            f.write(f"{text}\n")
            f.close()