from src.pyfilewatcher import FileWatcher

file = FileWatcher(name="Example", files=["example.log"], interval=1)
file()