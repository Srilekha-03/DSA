# Write your MySQL query statement below
SELECT E1.NAME
FROM Employee E1
JOIN (
    SELECT managerId,
           COUNT(*) AS dr
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) E2
ON E1.id = E2.managerId;
