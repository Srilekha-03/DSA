# Write your MySQL query statement below
with cte as ((select employee_id from Employees)
union
(select employee_id from Salaries))

select employee_id from cte 
where employee_id not in ((select employee_id from Employees)
intersect
(select employee_id from Salaries))
order by employee_id