CREATE TABLE IF NOT EXISTS Meal (
    meal_no CHAR(3) NOT NULL,
    type CHAR(20) NOT NULL CHECK(Type IN ("fish", "chicken", "beef", "vegetarian")),
    special_cuisine VARCHAR(20) CHECK(special_cuisine ~ '^[A-Za-z]+$'),
    dish_name VARCHAR(20) NOT NULL CHECK(dish_name ~ '^[A-Za-z]+$'),
    price INT NOT NULL CHECK(Price BETWEEN 100 AND 2000),
    PRIMARY KEY(meal_no),
)