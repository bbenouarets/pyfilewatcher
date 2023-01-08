from datetime import datetime
from src.pyfilewatcher import Watcher
from src.pyfilewatcher.handler import LogHandler

path = "test/example.txt"
date = datetime.now().strftime("%Y-%m-%d")
log = f"log/{date}.log"
callback = LogHandler(path=log)

monitor = Watcher(path=path, interval=1, callback=callback.write)
monitor.start()