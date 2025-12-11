# Write your MySQL query statement below
select name from SalesPerson
where sales_id not in (select o.sales_id as id
from Company c
left join
Orders o on c.com_id=o.com_id
where o.com_id = (select com_id from Company where name='RED'))