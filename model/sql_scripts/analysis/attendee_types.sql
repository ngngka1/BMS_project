SELECT type, COUNT(*) AS attendee_count
FROM Attendee
GROUP BY type;