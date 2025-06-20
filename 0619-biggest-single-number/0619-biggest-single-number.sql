# Write your MySQL query statement below
with cte as
(select num from MyNumbers 
group by num
having count(num)=1)

select case when count(*)>=1 then max(num)
else null end as num
from cte