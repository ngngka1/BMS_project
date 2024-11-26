import sqlite3
class Attendee:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attendee.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Attendee.__db_connection = db_connection
        Attendee.__db_connection.execute('''
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
        Attendee.__db_connection.commit()
    
    def insert(*args):
        Attendee.__db_connection.execute(f'''
            INSERT INTO Attendee VALUES ({args})
        ''')
        Attendee.__db_connection.commit()
        
        