import sqlite3
class AttendModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        AttendModel.db_connection = db_connection
        try:
            with open("./model/sql_scripts/attend/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = AttendModel.db_connection.cursor()
        cursor.execute(sql_command)
        # AttendModel.db_connection.commit()
    
    @staticmethod
    def insert(**kwargs):
        try:
            with open("./model/sql_scripts/attend/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = AttendModel.db_connection.cursor()
        cursor.execute(sql_command, kwargs)
        # AttendModel.db_connection.commit()