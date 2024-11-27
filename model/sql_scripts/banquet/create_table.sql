CREATE TABLE IF NOT EXISTS Banquet (
    bin INT NOT NULL CHECK(bin > 0),
    name VARCHAR(20) NOT NULL CHECK(name ~ '^[A-Za-z]+$');
    available BOOLEAN NOT NULL,
    quota INT NOT NULL CHECK(quota > 0),
    address VARCHAR(255) NOT NULL,
    location VARCHAR(6) NOT NULL,
    PRIMARY KEY(bin)
)