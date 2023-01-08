from src.pyfilewatcher import Observer

locations = [
    "test"
]

observer = Observer()
observer.watch(locs=locations)