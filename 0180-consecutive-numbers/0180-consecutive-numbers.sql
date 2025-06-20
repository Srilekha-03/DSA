# Write your MySQL query statement below
WITH ConsecutiveNumsCTE AS (
    SELECT 
        num,
        LEAD(num, 1) OVER() AS num1,
        LEAD(num, 2) OVER() AS num2
    FROM Logs
)
SELECT num AS ConsecutiveNums
FROM ConsecutiveNumsCTE
WHERE num = num1
  AND num = num2;
