import pymysql
from utils.error import ErrorSystem


class Database:
    def __init__(self, config_data):
        self.host = config_data["mysql_host"]
        self.port = config_data["mysql_port"]
        self.user = config_data["mysql_user"]
        self.password = config_data["mysql_password"]
        self.database = config_data["mysql_database"]

    def reload_configs(self, config_data):
        self.host = config_data["mysql_host"]
        self.port = config_data["mysql_port"]
        self.user = config_data["mysql_user"]
        self.password = config_data["mysql_password"]
        self.database = config_data["mysql_database"]

    def connect(self, database):
        connection = pymysql.connect(
            host=self.host,
            port=int(self.port),
            user=self.user,
            password=self.password,
            database=database,
        )
        return connection

    def execute(self, query):
        try:
            connection = self.connect(self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query)
            connection.commit()
        except Exception as error:
            ErrorSystem.open("Error:", error)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def execute_many(self, queries):
        connection = None
        try:
            connection = self.connect(self.database)
            cursor = connection.cursor()
            for query in queries:
                cursor.execute(query)
            connection.commit()
        except Exception as error:
            ErrorSystem.open("Error:", error)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def fetch(self, query, params=None):
        try:
            connection = self.connect(self.database)
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Exception as error:
            ErrorSystem.open("Error:", error)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
