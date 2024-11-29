SELECT m.dish_name, m.type, COUNT(p.meal_no) AS popularity
FROM Provide p
JOIN Meal m ON p.meal_no = m.meal_no
GROUP m.meal_no, m.dish_name, m.type
ORDER BY popularity DESC