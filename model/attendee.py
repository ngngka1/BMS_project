import sqlite3
from utils.auth.decorators import admin_required
from utils.exceptions.ForbiddenException import ForbiddenException
from settings import start_session, check_admin_mode, get_session_data
class AttendeeModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        AttendeeModel.__db_connection = db_connection
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        AttendeeModel.__db_connection.commit()
        
    @staticmethod
    def validate_session():
        if (check_admin_mode()):
            return
        if get_session_data("email_address") is None or get_session_data("password") is None:
            raise ForbiddenException("Please login first!")
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/query_user_by_credentials.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(**get_session_data()))
        result = cursor.fetchone()
        if result is None:
            return ["Invalid session"]
        
    @staticmethod
    def login(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/query_user_by_credentials.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(**kwargs))
        result = cursor.fetchone()
        if result is None:
            return ["Invalid username or password"]
        else:
            start_session(kwargs)
            return ["Login successful"]
    
    @staticmethod
    def insert(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs))
            AttendeeModel.__db_connection.commit()
            return ["Attendee record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @staticmethod
    def update(**kwargs):
        cursor = AttendeeModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/attendee/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(**kwargs))
            AttendeeModel.__db_connection.commit()
            return ["Attendee record updated successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @admin_required
    def get_information():
        pass
        return ["to be implemented"]
        
        