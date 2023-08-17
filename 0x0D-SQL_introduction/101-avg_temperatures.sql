-- task 18: for each city show average temperature in (Fahrenheit format)
-- order results by temp.(descending).
SELECT city, AVG(value) as avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
