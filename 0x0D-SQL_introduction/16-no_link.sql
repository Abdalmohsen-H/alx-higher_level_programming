-- task 16: show all records from table but exclude records missing value in name column
SELECT score, name FROM `second_table`
WHERE name IS NOT NULL
ORDER BY score DESC;
