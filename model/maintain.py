import sqlite3
class MaintainModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Maintain.__db_connection is None:
        #     raise Exception('Database connection already exists')
        MaintainModel.__db_connection = db_connection
        cursor = MaintainModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/maintain/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        MaintainModel.__db_connection.commit()
    
    def insert(*args):
        cursor = MaintainModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/maintain/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args))
        MaintainModel.__db_connection.commit()
        
        