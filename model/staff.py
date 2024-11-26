import sqlite3
class StaffModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Staff.__db_connection is None:
        #     raise Exception('Database connection already exists')
        StaffModel.__db_connection = db_connection
        StaffModel.__db_connection.execute('''
            CREATE TABLE Staff (
                Staff_No CHAR(8) NOT NULL,
                First_Name VARCHAR(20) NOT NULL,
                Last_Name VARCHAR(20) NOT NULL,
                Department CHAR(22) NOT NULL CHECK(Department IN ("Catering", "Events Services", "Kitchen Staff", "Bar Services", "Facilities Management", "Audio and Visual", "Decor and Design", "Guest Services", "Security")),            
                PRIMARY KEY(Staff_No)
                
            )
        ''')
        StaffModel.__db_connection.commit()
    
    def insert(*args):
        StaffModel.__db_connection.execute(f'''
            INSERT INTO Staff VALUES ({args})
        ''')
        StaffModel.__db_connection.commit()