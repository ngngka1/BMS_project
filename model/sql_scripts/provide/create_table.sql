CREATE TABLE IF NOT EXISTS Provide (
    bin INTEGER NOT NULL,
    meal_no INTEGER NOT NULL,
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (meal_no) REFERENCES Meal(meal_no),
    PRIMARY KEY (bin, meal_no)
)