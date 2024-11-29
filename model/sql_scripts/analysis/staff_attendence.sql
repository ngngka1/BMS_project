SELECT (COUNT(CASE WHEN m.present = 1 THEN 1 END) * 100.0 / COUNT(DISTINCT s.staff_no)) AS attendance_percentage
FROM Staff s
LEFT JOIN Maintain m ON s.staff_no = m.staff_no;