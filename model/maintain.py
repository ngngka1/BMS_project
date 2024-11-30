import sqlite3
from utils.auth.decorators import admin_required
from utils.miscellaneous.smart_sql_statement import update_statement_by_kwargs

class MaintainModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        MaintainModel.db_connection = db_connection
        cursor = MaintainModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        
        cursor.execute(sql_command)
        # MaintainModel.db_connection.commit()
    
    @staticmethod
    @admin_required
    def insert(**kwargs):
        cursor = MaintainModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs)
        
        
    @staticmethod
    @admin_required
    def update(**kwargs):
        cursor = MaintainModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/maintain/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(update_statement_by_kwargs(sql_command, **kwargs), kwargs)
        