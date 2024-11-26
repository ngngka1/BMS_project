import sqlite3
class AttendModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attend.__db_connection is None:
        #     raise Exception('Database connection already exists')
        AttendModel.__db_connection = db_connection
        try:
            with open("./sql_scripts/attend/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor = AttendModel.__db_connection.cursor()
        cursor.execute(sql_command)
        AttendModel.__db_connection.commit()
    
    def insert(*args):
        AttendModel.__db_connection.execute(f'''
            INSERT INTO Attend VALUES ({args})
        ''')
        AttendModel.__db_connection.commit()
        
        