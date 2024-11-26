import sqlite3
class Attend:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Attend.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Attend.__db_connection = db_connection
        Attend.__db_connection.execute('''
            CREATE TABLE Attend (
                BIN INT NOT NULL CHECK(BIN > 0),
                Email_Address VARCHAR(50) NOT NULL CHECK(Email_Address LIKE "%@%"),
                PRIMARY KEY (BIN, Email_Address),
                FOREIGN KEY (BIN) REFERENCES Banquet(BIN),
                FOREIGN KEY (Email_Address) REFERENCES Attendee(Email_Address)
            )
        ''')
        Attend.__db_connection.commit()
    
    def insert(*args):
        Attend.__db_connection.execute(f'''
            INSERT INTO Attend VALUES ({args})
        ''')
        Attend.__db_connection.commit()
        
        