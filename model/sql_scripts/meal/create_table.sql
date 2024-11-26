CREATE TABLE IF NOT EXISTS Meal (
    Meal_NO CHAR(3) NOT NULL,
    -- BIN INT NOT NULL CHECK(BIN > 0),
    Type CHAR(20) NOT NULL CHECK(Type IN ("fish", "chicken", "beef", "vegetarian")),
    Special_Cuisine VARCHAR(20) CHECK(Special_Cuisine ~ '^[A-Za-z]+$'),
    Dish_Name VARCHAR(20) NOT NULL CHECK(Dish_Name ~ '^[A-Za-z]+$'),
    Price INT NOT NULL CHECK(Price BETWEEN 100 AND 2000),
    PRIMARY KEY(Meal_NO, BIN),
    FOREIGN KEY(BIN) REFERENCES Banquet(BIN)
)