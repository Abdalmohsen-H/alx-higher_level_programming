-- task 11 : Select all records from table with a specific order, where score >= 10
-- while show only 2 selected columns from this table
SELECT score, name FROM `second_table`
WHERE score >= 10
ORDER BY `score` DESC;
