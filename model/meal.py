import sqlite3
class MealModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
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
        try:
            cursor.execute(sql_command.format(*args)) # **this part needs to format keyword arguments
            MealModel.__db_connection.commit()
            return ["Meal record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]