import sqlite3
class BanquetModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Banquet.__db_connection is None:
        #     raise Exception('Database connection already exists')
        BanquetModel.__db_connection = db_connection
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/banquet/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        BanquetModel.__db_connection.commit()
    
    def insert(*args):
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/banquet/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args)) # **this part needs to format keyword arguments
        BanquetModel.__db_connection.commit()
        
        