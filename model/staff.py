import sqlite3
class StaffModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Staff.__db_connection is None:
        #     raise Exception('Database connection already exists')
        StaffModel.__db_connection = db_connection
        cursor = StaffModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/staff/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        StaffModel.__db_connection.commit()
    
    def insert(*args):
        cursor = StaffModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/staff/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args))
        StaffModel.__db_connection.commit()