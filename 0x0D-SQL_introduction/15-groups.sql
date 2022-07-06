-- a script that lists the number of records
SELECT score, COUNT(score) AS NUMBER
from second_table GROUP BY score ORDER BY NUMBER DESC;
