SELECT s.first_name, s.last_name, COUNT(*) AS maintained_banquet ,ROUND(COUNT(*) * 100.0 / (
    SELECT COUNT(*)
    FROM Staff s, Maintain m, Banquet b
    WHERE m.bin = b.bin
    AND s.staff_no = m.staff_no
    GROUP BY s.staff_no
), 2) AS attendance_percentage
FROM Staff s, Maintain m, Banquet b
WHERE m.bin = b.bin
AND s.staff_no = m.staff_no
AND b.date_and_time < DATETIME('now')
AND m.present = 1
GROUP BY s.staff_no
ORDER BY attendance_percentage DESC;