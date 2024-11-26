CREATE TABLE IF NOT EXISTS Attend (
    BIN INT NOT NULL CHECK(BIN > 0),
    Email_Address VARCHAR(50) NOT NULL CHECK(Email_Address LIKE "%@%"),
    PRIMARY KEY (BIN, Email_Address),
    FOREIGN KEY (BIN) REFERENCES Banquet(BIN),
    FOREIGN KEY (Email_Address) REFERENCES Attendee(Email_Address)
)