# Write your MySQL query statement below
with cte as(select requester_id as user 
from RequestAccepted 
union all
select accepter_id as user 
from RequestAccepted),

cte1 as (select user,count(*) as count from cte
group by user)

select user as id,count as num from cte1
order by count desc limit 1;