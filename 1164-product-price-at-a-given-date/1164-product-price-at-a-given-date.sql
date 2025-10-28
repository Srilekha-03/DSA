# Write your MySQL query statement below
with cte as (select product_id,new_price as price from (select * ,
rank() over(partition by product_id order by change_date desc) as rnk
from Products
WHERE change_date <= '2019-08-16') as x
where x.rnk=1)

select * from cte
union
select product_id,10 as price 
from Products
where product_id not in (select product_id from cte)