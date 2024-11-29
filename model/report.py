import sqlite3
class ReportModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        ReportModel.__db_connection = db_connection
        
    @staticmethod
    def attendee_types():
        cursor = ReportModel.__db_connection.cursor()
        try:
            with open("./model/sql_scripts/analysis/attendee_types.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()