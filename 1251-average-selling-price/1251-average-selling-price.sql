# Write your MySQL query statement below
select p.product_id, round(
    case when sum(u.units)=0 or sum(u.units) is null then  0
    else sum(u.units*p.price)/sum(units) end, 2)as average_price
from Prices p
left join UnitsSold u
on p.product_id=u.product_id
and u.purchase_date between p.start_date and p.end_date
group by product_id