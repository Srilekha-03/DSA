# Write your MySQL query statement below
with cte as ((select product_id as product_id,
case 
    when store1 is not null then 'store1'
end as store, store1 as price
from Products)
union
(select product_id as product_id,
case 
    when store2 is not null then 'store2'
end as store, store2 as price
from Products)
union
(select product_id as product_id,
case 
    when store3 is not null then 'store3'
end as store, store3 as price
from Products)
order by product_id,store)
select product_id,store,price from cte where store is not null or price is not null


        
