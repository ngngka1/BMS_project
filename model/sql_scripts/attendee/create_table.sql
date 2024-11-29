CREATE TABLE IF NOT EXISTS Attendee (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    email_address VARCHAR(50) UNIQUE NOT NULL CHECK(email_address LIKE "%@%"),
    password VARCHAR(20) NOT NULL , -- ON UPDATE RESTRICT
    first_name VARCHAR(20) NOT NULL CHECK(first_name REGEXP '^[A-Za-z]+$'),
    last_name VARCHAR(20) NOT NULL CHECK(last_name REGEXP '^[A-Za-z]+$'),
    type VARCHAR(7) NOT NULL CHECK(LOWER(type) IN ("staff", "student", "alumni", "guest")),
    phone_no CHAR(8) NOT NULL CHECK(LENGTH(phone_no) = 8 AND phone_no REGEXP '^[0-9]+$'),
    address VARCHAR(255) NOT NULL,
    organization VARCHAR(40) NOT NULL
)
