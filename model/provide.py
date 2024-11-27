import sqlite3
class ProvideModel:
    __db_connection = None
    def __init__(self, db_connection: sqlite3.Connection):
        ProvideModel.__db_connection = db_connection
        try:
            with open("./sql_scripts/provide/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor = ProvideModel.__db_connection.cursor()
        cursor.execute(sql_command)
        ProvideModel.__db_connection.commit()
    
    