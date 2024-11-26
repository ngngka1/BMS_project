CREATE TABLE IF NOT EXISTS Staff (
    Staff_No CHAR(8) NOT NULL,
    First_Name VARCHAR(20) NOT NULL,
    Last_Name VARCHAR(20) NOT NULL,
    Department CHAR(22) NOT NULL CHECK(Department IN ("Catering", "Events Services", "Kitchen Staff", "Bar Services", "Facilities Management", "Audio and Visual", "Decor and Design", "Guest Services", "Security")),            
    PRIMARY KEY(Staff_No)
    
)