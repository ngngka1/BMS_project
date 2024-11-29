import sqlite3
class ProvideModel:
    db_connection = None
    def __init__(self, db_connection: sqlite3.Connection):
        ProvideModel.db_connection = db_connection
        try:
            with open("./model/sql_scripts/provide/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor = ProvideModel.db_connection.cursor()
        cursor.execute(sql_command)
        # ProvideModel.db_connection.commit()
        
    @staticmethod
    def insert(**kwargs):
        cursor = ProvideModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/provide/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs) # **this part needs to format keyword arguments
        # ProvideModel.db_connection.commit()
    
    