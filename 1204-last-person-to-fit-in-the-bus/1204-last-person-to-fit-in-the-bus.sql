# Write your MySQL query statement below
with cte as (SELECT
    person_id,
    person_name,
    weight,
    turn,
    SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
FROM Queue)

select person_name 
from cte 
where cumulative_weight<=1000
ORDER BY turn desc
LIMIT 1;

