CREATE TABLE IF NOT EXISTS Maintain (
    present BOOLEAN,
    bin INTEGER NOT NULL,
    staff_no INTEGER NOT NULL,
    FOREIGN KEY (bin) REFERENCES Banquet(bin),
    FOREIGN KEY (staff_no) REFERENCES Staff(staff_no),
    PRIMARY KEY (bin, staff_no)
)