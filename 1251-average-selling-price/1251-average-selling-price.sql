# Write your MySQL query statement below
# Write your MySQL query statement below
select p.product_id, IFNULL(round(sum(u.units*p.price)/sum(units),2),0) as average_price
from Prices p
left join UnitsSold u
on p.product_id=u.product_id
where u.purchase_date between p.start_date and p.end_date
group by product_id