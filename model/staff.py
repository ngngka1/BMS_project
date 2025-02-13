import sqlite3
from utils.auth.decorators import admin_required
from utils.miscellaneous.smart_sql_statement import update_statement_by_kwargs
class StaffModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        StaffModel.db_connection = db_connection
        cursor = StaffModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        # StaffModel.db_connection.commit()
        
    @staticmethod
    @admin_required
    def list_all():
        cursor = StaffModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/query_all.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()
    
    @staticmethod
    @admin_required
    def insert(**kwargs):
        cursor = StaffModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs)
        # StaffModel.db_connection.commit()
        print(f"Staff record with staff_no {cursor.lastrowid} created successfully")
        
    @staticmethod
    @admin_required
    def update(**kwargs):
        cursor = StaffModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/staff/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(update_statement_by_kwargs(sql_command, **kwargs), kwargs)
        # StaffModel.db_connection.commit()
        print(f"Staff record with staff_no {kwargs['staff_no']} updated successfully")
        
    