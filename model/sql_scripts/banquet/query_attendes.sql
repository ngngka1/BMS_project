SELECT *
FROM Attendee a, Banquet b, Attend att
WHERE a.attendeeID = att.attendeeID
AND b.banquetID = att.banquetID
AND b.banquetID = :bin;