-- task 19:  show only 3 cities that have highest temperature during months: July and August
-- order results by tempe. (descending)
SELECT city, AVG(value) as avg_temp FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
