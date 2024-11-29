import sqlite3
class MaintainModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        MaintainModel.db_connection = db_connection
        cursor = MaintainModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        
        cursor.execute(sql_command)
        # MaintainModel.db_connection.commit()
    
    @staticmethod
    def insert(**kwargs):
        cursor = MaintainModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs) # **this part needs to format keyword arguments
        
        