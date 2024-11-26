import sqlite3
from utils.auth.decorators import admin_required

class BanquetModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        BanquetModel.__db_connection = db_connection
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/banquet/create_table.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        cursor.execute(sql_command)
        BanquetModel.__db_connection.commit()
    
    @admin_required
    def insert(*args):
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/banquet/insert.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(*args)) # **this part needs to format keyword arguments
            BanquetModel.__db_connection.commit()
            return ["Banquet record created successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]
        
    @admin_required
    def update(*args):
        cursor = BanquetModel.__db_connection.cursor()
        try:
            with open("./sql_scripts/banquet/update.sql", "r") as f:
                sql_command = f.read()
        except:
            raise Exception("Failed to read sql script")
        try:
            cursor.execute(sql_command.format(*args)) # **this part needs to format keyword arguments
            BanquetModel.__db_connection.commit()
            return ["Banquet record updated successfully"]
        except sqlite3.IntegrityError as e:
            return ["Integerity error: " + e]