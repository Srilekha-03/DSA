# Write your MySQL query statement below
WITH CTE AS (
    SELECT customer_number,Count(order_number) as ord_count
    FROM ORDERS 
    GROUP BY customer_number
)
SELECT customer_number
FROM CTE WHERE ord_count = (SELECT MAX(ord_count) from CTE)