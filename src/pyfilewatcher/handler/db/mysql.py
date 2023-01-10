import mysql.connector as mysql

class MySQLDatabase:
    def __init__(self, connection: dict) -> None:
        self.__cred = connection
        self.__db_host = connection["host"]
        self.__db_port = connection["port"]
        self.__db_username = connection["user"]
        self.__db_password = connection["password"]
        self.__db_database = connection["database"]
        self.connect()

    def connect(self) -> None:
        try:
            self.cnx = mysql.connect(
                host=self.__db_host,
                port=self.__db_port,
                user=self.__db_username,
                password=self.__db_password,
                database=self.__db_database
            )
            print("Connection to mysql database established!")
        except mysql.connector.ConnectError as err:
            print(err)

    def write(self, id: int, file: str, job: str = "observer") -> None:
        cursor = self.cnx.cursor()
        __message = "File changed"
        __data = (id, job, file, __message)
        __job = "INSERT INTO observe (thread, job, file, message) VALUE (%s, %s, %s, %s)"
        cursor.execute(__job, __data)
        self.cnx.commit()
        cursor.close()