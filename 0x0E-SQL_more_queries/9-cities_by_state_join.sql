-- task 8 : Display results info from two tables using join statement
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id=states.id
ORDER BY cities.id ASC;
