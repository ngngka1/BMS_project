UPDATE Attendee SET (
    {email_address},
    (
        SELECT password
        FROM Attendee
        WHERE email_address = {email_address}
    ),
    {first_name},
    {last_name},
    {type},
    {phone_no},
    {address},
    {organization}
)