import sqlite3
class ReportModel:
    db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        ReportModel.db_connection = db_connection
        
    @staticmethod
    def attendee_types():
        cursor = ReportModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/analysis/attendee_types.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()
    
    @staticmethod
    def attendance():
        cursor = ReportModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/analysis/attendance_behavior.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()
    
    @staticmethod
    def popular_meals():
        cursor = ReportModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/analysis/most_popular_meals.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()
    
    @staticmethod
    def staff_attendance():
        cursor = ReportModel.db_connection.cursor()
        try:
            with open("./model/sql_scripts/analysis/staff_attendance.sql", "r") as f:
                sql_command = f.read()
        except:
            raise OSError("Failed to read sql script")
        cursor.execute(sql_command)
        return cursor.fetchall()