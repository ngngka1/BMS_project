import sqlite3
from utils.miscellaneous.smart_update_statement import update_statement_by_kwargs
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
        
    @staticmethod
    def update(**kwargs):
        try:
            with open("./model/sql_scripts/attend/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = AttendModel.db_connection.cursor()
        updating_fields = kwargs.copy()
        updating_fields.pop("bin")
        updating_fields.pop("account_id")
        
        cursor.execute(update_statement_by_kwargs(sql_command, **updating_fields), kwargs)