import sqlite3
class MealModel:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Meal.__db_connection is None:
        #     raise Exception('Database connection already exists')
        MealModel.__db_connection = db_connection
        MealModel.__db_connection.execute('''
            CREATE TABLE Meal (
                Meal_NO CHAR(3) NOT NULL,
                BIN INT NOT NULL,
                Type CHAR(20) NOT NULL CHECK(Meal_Type IN ("fish", "chicken", "beef", "v")),
                Phone_No VARCHAR(20) NOT NULL CHECK(Phone_Number LIKE '+% %'),
                Address VARCHAR(255) NOT NULL,
                Organization VARCHAR(40) NOT NULL,
                PRIMARY KEY(Email_Address)
                
            )
        ''')
        MealModel.__db_connection.commit()
    
    def insert(*args):
        MealModel.__db_connection.execute(f'''
            INSERT INTO Meal VALUES ({args})
        ''')
        MealModel.__db_connection.commit()