import sqlite3
from utils.auth.decorators import admin_required
class AttendeeModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attendee.__db_connection is None:
        #     raise Exception('Database connection already exists')
        AttendeeModel.__db_connection = db_connection
        cursor = AttendeeModel.__db_connection.cursor()
        cursor.execute('''
            CREATE TABLE Attendee (
                Email_Address VARCHAR(255) PRIMARY KEY NOT NULL,
                Email_Password VARCHAR(255) NOT NULL,
                First_Name VARCHAR(255) NOT NULL,
                Last_Name VARCHAR(255) NOT NULL,
                Type VARCHAR(255) NOT NULL,
                Phone_No VARCHAR(255) NOT NULL,
                Address VARCHAR(255) NOT NULL,
                Organization VARCHAR(255) NOT NULL,
                CHECK ()
            )
        ''')
        AttendeeModel.__db_connection.commit()
    
    def insert(*args):
        cursor = AttendeeModel.__db_connection.cursor()
        cursor.execute(f'''
            INSERT INTO Attendee VALUES ({args})
        ''')
        AttendeeModel.__db_connection.commit()
        return ["Attendee record created successfully"]
        
    def update(*args):
        cursor = AttendeeModel.__db_connection.cursor()
        cursor.execute(f'''
            UPDATE Attendee SET {args}
        ''')
        AttendeeModel.__db_connection.commit()
        return ["Attendee record updated successfully"]
        
    @admin_required
    def get_information():
        pass
        return ["to be implemented"]
        
        