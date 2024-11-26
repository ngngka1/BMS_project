CREATE TABLE Banquet (
    BIN INT NOT NULL CHECK(BIN > 0),
    Banquet_Name VARCHAR(20) NOT NULL CHECK(Banquet_Name ~ '^[A-Za-z]+$');
    Available BOOLEAN NOT NULL,
    Quota INT NOT NULL CHECK(Quota > 0),
    Address VARCHAR(255) NOT NULL,
    Location VARCHAR(6) NOT NULL,
    PRIMARY KEY(BIN)
)