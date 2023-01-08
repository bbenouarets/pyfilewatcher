import mysql.connector as mysql

class MySQLDatabase:
    def __init__(self, connection: dict) -> None:
        self.__cred = connection
        self.__db_host = connection["host"]
        self.__db_port = connection["port"]
        self.__db_username = connection["username"]
        self.__db_password = connection["password"]
        self.__db_database = connection["database"]

    def connect(self) -> None:
        self.cnx = mysql.connect(
            host=self.__db_host,
            port=self.__db_port,
            user=self.__db_username,
            password=self.__db_password,
            database=self.__db_database
        )
        self.cnx.connect()
        