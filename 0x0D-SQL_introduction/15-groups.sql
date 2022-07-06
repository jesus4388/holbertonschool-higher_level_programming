-- a script that lists the number of records
SELECT score, COUNT(score) AS number from second_table GROUP BY score ORDER BY number DESC;
