# Write your MySQL query statement below
SELECT
    CASE
        WHEN id % 2 != 0 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        WHEN id % 2 = 0 THEN id - 1
        WHEN id % 2 != 0 THEN id + 1
    END AS id,
    student
FROM
    Seat
ORDER BY
    id;