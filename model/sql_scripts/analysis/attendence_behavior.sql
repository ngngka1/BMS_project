SELECT 
    Banquet.name AS banquet_name,
    Attendee.email_address,
    Attendee.first_name,
    Attendee.last_name,
    Attendee.phone_no,
    Attend.present,
    Attend.drink_choice,
    Attend.meal_choice,
    Attend.remarks
FROM Attend
JOIN Attendee ON Attend.email_address = Attendee.email_address
JOIN Banquet ON Attend.bin = Banquet.bin
ORDER BY Banquet.name, Attendee.last_name, Attendee.first_name;