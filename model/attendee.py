import sqlite3
class Attendee:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attendee.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Attendee.__db_connection = db_connection
        Attendee.__db_connection.execute('''
            CREATE TABLE Attendee (
                Email_Address VARCHAR(50) NOT NULL CHECK(Email_Address LIKE "%@%"),
                Email_Password VARCHAR(20) NOT NULL,
                First_Name VARCHAR(20) NOT NULL CHECK(First_Name ~ '^[A-Za-z]+$'),
                Last_Name VARCHAR(20) NOT NULL CHECK(Last_Name ~ '^[A-Za-z]+$'),
                Type CHAR(7) NOT NULL CHECK(Type IN ("Staff", "Student", "Alumni", "Guest")),
                Phone_No CHAR(8) NOT NULL CHECK(LENGTH(Phone_No) = 8 AND Phone_No NOT LIKE '% '),
                Address VARCHAR(255) NOT NULL,
                Organization CHAR(6) NOT NULL CHECK("PolyU", "SPEED", "HKCC", "Others"),
                PRIMARY KEY(Email_Address)    
            )
        ''')
        Attendee.__db_connection.commit()
    
    def insert(*args):
        Attendee.__db_connection.execute(f'''
            INSERT INTO Attendee VALUES ({args})
        ''')
        Attendee.__db_connection.commit()
        
        