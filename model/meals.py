import sqlite3
class Meal:
    __db_connection = None
    
    def __init__(self, db_connection: sqlite3.Connection):
        # if not Meal.__db_connection is None:
        #     raise Exception('Database connection already exists')
        Meal.__db_connection = db_connection
        Meal.__db_connection.execute('''
            CREATE TABLE Meal (
                Meal_NO CHAR(3) NOT NULL,
                BIN INT NOT NULL CHECK(BIN > 0),
                Type CHAR(20) NOT NULL CHECK(Type IN ("fish", "chicken", "beef", "vegetarian")),
                Special_Cuisine VARCHAR(20) CHECK(Special_Cuisine ~ '^[A-Za-z]+$'),
                Dish_Name VARCHAR(20) NOT NULL CHECK(Dish_Name ~ '^[A-Za-z]+$'),
                Price INT NOT NULL CHECK(Price BETWEEN 100 AND 2000),
                PRIMARY KEY(Meal_NO, BIN),
                FOREIGN KEY(BIN) REFERENCES Banquet(BIN)
            )
        ''')
        Meal.__db_connection.commit()
    
    def insert(*args):
        Meal.__db_connection.execute(f'''
            INSERT INTO Meal VALUES ({args})
        ''')
        Meal.__db_connection.commit()
        
        