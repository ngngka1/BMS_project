CREATE TABLE IF NOT EXISTS Banquet (
    bin INTEGER PRIMARY KEY AUTOINCREMENT,
    date_and_time VARCHAR(20) NOT NULL CHECK(date_and_time REGEXP '^[0-9]{4}[-][0-9]{2}[-][0-9]{2} [0-9]{2}[:][0-9]{2}[:][0-9]{2}$'),
    name VARCHAR(20) NOT NULL CHECK(name REGEXP '^[A-Za-z]+$'),
    available BOOLEAN NOT NULL,
    quota INT NOT NULL CHECK(quota >= 0),
    address VARCHAR(255) NOT NULL,
    location VARCHAR(6) NOT NULL
    -- PRIMARY KEY(bin)
)

