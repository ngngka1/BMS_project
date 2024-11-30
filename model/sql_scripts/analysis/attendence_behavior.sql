SELECT 
    Banquet.name AS banquet_name,
    Banquet.date_and_time AS banquet_date_and_time,
    Banquet.location AS banquet_location,
    ROUND((COUNT(*) * 100.0) / (
        SELECT COUNT(*)
        FROM Attend, Banquet
        WHERE Attend.bin = Banquet.bin
    )
    , 2) AS attendence_percentage
FROM Attend, Banquet
WHERE Banquet.date_and_time < DATETIME('now')
AND Attend.bin = Banquet.bin
AND Attend.present = 1
GROUP BY Banquet.bin
ORDER BY attendence_percentage DESC;