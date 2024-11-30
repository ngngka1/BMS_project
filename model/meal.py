import sqlite3
from utils.auth.decorators import admin_required
from utils.miscellaneous.smart_sql_statement import update_statement_by_kwargs
class MealModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        MealModel.db_connection = db_connection
        cursor = MealModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        # MealModel.db_connection.commit()
        
    @staticmethod
    def list_all():
        cursor = MealModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/query_all.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()
    
    @staticmethod
    @admin_required
    def insert(**kwargs):
        cursor = MealModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command, kwargs) # **this part needs to format keyword arguments
        # MealModel.db_connection.commit()
        print(f"Meal record with meal_no {cursor.lastrowid} created successfully")
        
    @staticmethod
    @admin_required
    def update(**kwargs):
        cursor = MealModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/meal/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        
        cursor.execute(update_statement_by_kwargs(sql_command, **kwargs), kwargs) # **this part needs to format keyword arguments
        # MealModel.db_connection.commit()