import sqlite3
class Banquet:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Banquet.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Banquet.__db_connection = db_connection
        Banquet.__db_connection.execute('''
            CREATE TABLE Banquet (
              BIN INT NOT NULL CHECK(BIN > 0),
              Banquet_Name VARCHAR(20) NOT NULL CHECK(Banquet_Name ~ '^[A-Za-z]+$');
              Available BOOLEAN NOT NULL,
              Quota INT NOT NULL CHECK(Quota > 0),
              Address VARCHAR(255) NOT NULL,
              Location VARCHAR(6) NOT NULL,
              PRIMARY KEY(BIN)
            )
        ''')
        Banquet.__db_connection.commit()
    
    def insert(*args):
        Banquet.__db_connection.execute(f'''
            INSERT INTO Banquet VALUES ({args})
        ''')
        Banquet.__db_connection.commit()
        
        