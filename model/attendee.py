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
                Email_Address VARCHAR(50) NOT NULL CHECK(Email_Address LIKE "%@%"),
                Email_Password VARCHAR(20) NOT NULL,
                First_Name VARCHAR(20) NOT NULL CHECK(First_Name ~ '^[A-Za-z]+$'),
                Last_Name VARCHAR(20) NOT NULL CHECK(Last_Name ~ '^[A-Za-z]+$'),
                Type CHAR(7) NOT NULL CHECK(Type IN ("Staff", "Student", "Alumni", "Guest")),
                Phone_No CHAR(8) NOT NULL CHECK(LENGTH(Phone_No) = 8 AND Phone_No NOT LIKE '% '),
                Address VARCHAR(255) NOT NULL,
                Organization VARCHAR(40) NOT NULL,
                PRIMARY KEY(Email_Address)
                
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
        
        