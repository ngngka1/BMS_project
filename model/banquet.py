import sqlite3
from utils.auth.decorators import admin_required, authenticated_required
from utils.miscellaneous.smart_sql_statement import update_statement_by_kwargs, query_statement_by_kwargs

class BanquetModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        BanquetModel.db_connection = db_connection
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        # BanquetModel.db_connection.commit()
        
    @staticmethod
    @admin_required
    def get_attendees(bin_id: int):
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/query_attendees.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, {"bin": bin_id})
        return cursor.fetchall()
        
    @staticmethod
    @authenticated_required
    def get_one(bin_id: int):
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/query_by_bin.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, {"bin": bin_id})
        return cursor.fetchone()
        
    @staticmethod
    @authenticated_required
    def list_all(**kwargs):
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/query_all.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(query_statement_by_kwargs(sql_command, **kwargs))
        return cursor.fetchall()
        
    @staticmethod
    @admin_required
    def insert(return_pk=False, **kwargs):
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs)
        if return_pk:
            return cursor.lastrowid
        
    @staticmethod
    # @authenticated_required
    def update(**kwargs):
        cursor = BanquetModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/banquet/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        print("kwargs for update banquet:", kwargs)
        cursor.execute(update_statement_by_kwargs(sql_command, **kwargs), kwargs) # **this part needs to format keyword arguments