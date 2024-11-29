import sqlite3
class AttendModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        AttendModel.__db_connection = db_connection
        try:
            with open("./model/sql_scripts/attend/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = AttendModel.__db_connection.cursor()
        cursor.execute(sql_command)
        AttendModel.__db_connection.commit()
    
    @staticmethod
    def insert(**kwargs):
        try:
            with open("./model/sql_scripts/attend/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = AttendModel.__db_connection.cursor()
        cursor.execute(sql_command, kwargs)
        AttendModel.__db_connection.commit()