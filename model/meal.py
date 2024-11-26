import sqlite3
class MealModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Meal.__db_connection is None:
        #     raise Exception('Database connection already exists')
        MealModel.__db_connection = db_connection
        cursor = MealModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/meal/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        MealModel.__db_connection.commit()
    
    def insert(*args):
        cursor = MealModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/meal/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command.format(*args))
        MealModel.__db_connection.commit()