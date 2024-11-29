import sqlite3
from utils.auth.decorators import admin_required, authenticated_required
from utils.exceptions.ForbiddenException import ForbiddenException
from settings import start_session
from utils.miscellaneous.smart_update_statement import update_statement_by_kwargs
class AttendeeModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        AttendeeModel.db_connection = db_connection
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        # AttendeeModel.db_connection.commit()
        
    @staticmethod
    def login(**kwargs):
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/auth/query_user_by_credentials.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs)
        result = cursor.fetchone()
        if result is None:
            print("Invalid username or password")
        else:
            kwargs["account_id"] = result["account_id"]
            start_session(**kwargs)
            print("Login successful")
    
    @staticmethod
    def insert(**kwargs):
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs)
        # AttendeeModel.db_connection.commit()
        print("Attendee record created successfully")
        
    @staticmethod
    def update(**kwargs):
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        updating_fields = kwargs.copy()
        updating_fields.pop("old_email_address")
        cursor.execute(update_statement_by_kwargs(sql_command, **updating_fields), kwargs)
        # AttendeeModel.db_connection.commit()
        print("Attendee record updated successfully")
        
    @staticmethod
    @authenticated_required
    def get_information_by_email(email_address):
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/query_by_email.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, {"email_address": email_address})
        return cursor.fetchall()
        
    @staticmethod
    @admin_required
    def update_information_by_email(**kwargs):
        cursor = AttendeeModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/attendee/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(update_statement_by_kwargs(sql_command, **kwargs), kwargs)
        print(f"attendee with email={kwargs['email_address']} information updated")
        
        