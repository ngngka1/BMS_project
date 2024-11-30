SELECT m.dish_name, m.type, m.special_cuisine, COUNT(p.meal_no) AS popularity
FROM Provide p
JOIN Meal m ON p.meal_no = m.meal_no
GROUP BY m.meal_no, m.dish_name, m.type
ORDER BY popularity DESC;