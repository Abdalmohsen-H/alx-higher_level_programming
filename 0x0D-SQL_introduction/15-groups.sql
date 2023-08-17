-- task 15: group score values and show of each grouped value in specific order from specific table
SELECT `score`,
COUNT(*) as number
FROM `second_table`
group by `score`
order by number DESC;
