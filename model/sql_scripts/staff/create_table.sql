CREATE TABLE IF NOT EXISTS Staff (
    staff_no INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    department VARCHAR(22) NOT NULL CHECK(LOWER(department) IN ("catering", "events services", "kitchen staff", "bar services", "facilities management", "audio and visual", "decor and design", "guest services", "security"))           
)