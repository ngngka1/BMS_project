CREATE TABLE IF NOT EXISTS Attend (
    bin INTEGER NOT NULL,
    account_id INTEGER NOT NULL,
    present BOOLEAN,
    drink_choice VARCHAR(255),
    meal_choice VARCHAR(255),
    remarks VARCHAR(255),
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (account_id) REFERENCES Attendee(account_id),
    PRIMARY KEY (bin, account_id)
)