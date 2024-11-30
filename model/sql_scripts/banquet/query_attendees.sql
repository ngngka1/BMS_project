SELECT a.account_id, a.email_address, a.first_name, a.last_name, a.type, a.phone_no, a.organization, att.drink_choice, att.meal_choice, att.remarks, att.present
FROM Attendee a, Banquet b, Attend att
WHERE a.account_id = att.account_id
AND b.bin = att.bin
AND b.bin = :bin;