SELECT s.first_name, s.last_name, ROUND(COUNT(*) * 100.0 / (
    SELECT COUNT(*)
    FROM Staff s, Maintain m
    WHERE s.staff_no = m.staff_no
    GROUP BY s.staff_no
), 2) || '%' AS attendence_percentage
FROM Staff s, Maintain m
WHERE s.staff_no = m.staff_no
AND m.present = 1
GROUP BY s.staff_no
ORDER BY attendence_percentage DESC;