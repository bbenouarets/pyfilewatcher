import os
import sys
import configparser

from .watcher import Watcher
from .handler import Log, MySQLDatabase

class Observer:
    def __init__(self, config: str = "config/observer.conf") -> None:
        __handler = ["log", "mysql"]
        if config is None:
            self.config = input("Path: ")
        self.config = config
        data = self.__config()
        self.interval = data["interval"]
        self.__depth = data["depth"]
        self.__files = []
        if data["handler"] in __handler:
            if data["handler"] == "log":
                self.__callback = self.__log()
            if data["handler"] == "mysql":
                self.__callback = self.__mysql()

    def __config(self) -> dict:
        __config = configparser.ConfigParser()
        __config.read(self.config)
        return {
            "interval": int(__config["Default"]["INTERVAL"]),
            "depth": int(__config["Default"]["DEPTH"]),
            "handler": __config["Default"]["HANDLER"],
        }

    def __log(self) -> callable:
        __config = configparser.ConfigParser()
        __config.read(self.config)
        path = __config["log"]["PATH"]
        self.__handler = Log(path)
        return self.__handler.write

    def __mysql(self) -> dict:
        __config = configparser.ConfigParser()
        __config.read(self.config)
        cnx = {
            "host": __config["mysql"]["host"],
            "port": __config["mysql"]["port"],
            "user": __config["mysql"]["user"],
            "password": __config["mysql"]["password"],
            "database": __config["mysql"]["database"]
        }
        self.__handler = MySQLDatabase(connection=cnx)
        return self.__handler.write
        

    def files(self, path: str) -> list:
        x = []
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=True):
                if root.count(os.sep) > self.__depth:
                    dirs.clear()
                    continue
                for name in files:
                    f = os.path.join(root, name)
                    x.append(f)
        else:
            x = path
        return x

    def watch(self, locs: list) -> list:
        self.threads = []
        for loc in locs:
            __path = self.files(loc)
            for p in __path:
                self.__files.append(p)
        print(self.__files)
        for file in self.__files:
            watcher = Watcher(file=file, interval=self.interval, callback=self.__callback)
            watcher.start()
            self.threads.append(watcher.native_id)
        return self.threads

    def __call__(self, text) -> None:
        self.__callback(text)