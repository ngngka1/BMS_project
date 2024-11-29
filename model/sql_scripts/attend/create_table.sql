CREATE TABLE IF NOT EXISTS Attend (
    bin INTEGER NOT NULL,
    email_address VARCHAR(255) NOT NULL,
    drink_choice VARCHAR(255),
    meal_choice VARCHAR(255),
    remarks VARCHAR(255) NOT NULL,
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (email_address) REFERENCES Attendee(email_address),
    PRIMARY KEY (bin, email_address)
)