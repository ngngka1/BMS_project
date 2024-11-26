import sqlite3
from utils.auth.decorators import admin_required
class AttendeeModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attendee.__db_connection is None:
        #     raise Exception('Database connection already exists')
        AttendeeModel.__db_connection = db_connection
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        AttendeeModel.__db_connection.commit()
    
    def insert(*args):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args))
        AttendeeModel.__db_connection.commit()
        return ["Attendee record created successfully"]
        
    def update(*args):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args))
        AttendeeModel.__db_connection.commit()
        return ["Attendee record updated successfully"]
        
    @admin_required
    def get_information():
        pass
        return ["to be implemented"]
        
        