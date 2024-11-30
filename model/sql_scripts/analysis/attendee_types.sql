SELECT type, ROUND((COUNT(*) * 100.0 / (
    SELECT COUNT(account_id) FROM Attendee
)), 2) AS attendee_percentage,
    ROUND((
        SELECT COUNT(*)
        FROM Attendee, Attend
        WHERE Attendee.account_id = Attend.account_id
        AND Attend.present = 1
    ) * 100.0 / COUNT(*), 2) AS attendance_percentage
FROM Attendee
GROUP BY type
ORDER BY attendee_percentage DESC;