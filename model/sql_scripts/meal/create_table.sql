CREATE TABLE IF NOT EXISTS Meal (
    meal_no INTEGER PRIMARY KEY AUTOINCREMENT,
    type VARCHAR(20) NOT NULL CHECK(type IN ("fish", "chicken", "beef", "vegetarian")),
    special_cuisine BOOLEAN Not NULL,
    dish_name VARCHAR(20) NOT NULL CHECK(dish_name REGEXP '^[A-Za-z]+$'),
    price INT NOT NULL CHECK(price BETWEEN 100 AND 2000)
)