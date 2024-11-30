SELECT type, ROUND((COUNT(*) * 100.0 / (
    SELECT COUNT(account_id) FROM Attendee
)), 2) AS attendee_percentage
FROM Attendee
GROUP BY type
ORDER BY attendee_percentage DESC;