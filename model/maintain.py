import sqlite3
class Maintain:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Maintain.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Maintain.__db_connection = db_connection
        Maintain.__db_connection.execute('''
            CREATE TABLE Maintain (
                BIN INT NOT NULL CHECK(BIN > 0),
                Staff_No CHAR(8) NOT NULL,
                Present BOOLEAN NOT NULL,
                PRIMARY KEY (BIN, Staff_No),
                FOREIGN KEY (BIN) REFERENCES Banquet(BIN),
                FOREIGN KEY (Staff_No) REFERENCES Staff(Staff_No)
            )
        ''')
        Maintain.__db_connection.commit()
    
    def insert(*args):
        Maintain.__db_connection.execute(f'''
            INSERT INTO Maintain VALUES ({args})
        ''')
        Maintain.__db_connection.commit()
        
        