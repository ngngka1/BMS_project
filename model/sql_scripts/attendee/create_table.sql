CREATE TABLE IF NOT EXISTS Attendee (
    Email_Address VARCHAR(50) NOT NULL CHECK(Email_Address LIKE "%@%"),
    password VARCHAR(20) NOT NULL,
    First_Name VARCHAR(20) NOT NULL CHECK(First_Name ~ '^[A-Za-z]+$'),
    Last_Name VARCHAR(20) NOT NULL CHECK(Last_Name ~ '^[A-Za-z]+$'),
    Type CHAR(7) NOT NULL CHECK(Type IN ("Staff", "Student", "Alumni", "Guest")),
    Phone_No CHAR(8) NOT NULL CHECK(LENGTH(Phone_No) = 8 AND Phone_No NOT LIKE '% '),
    Address VARCHAR(255) NOT NULL,
    Organization VARCHAR(40) NOT NULL,
    PRIMARY KEY(Email_Address)
)
