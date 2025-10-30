# Write your MySQL query statement below
WITH cte AS (
    SELECT 
        u.name AS name,
        COUNT(m.movie_id) AS cnt
    FROM MovieRating m
    JOIN Users u ON u.user_id = m.user_id
    GROUP BY u.user_id, u.name
),
cte2 AS (
    SELECT 
        m.title AS title,
        AVG(r.rating) AS avr
    FROM MovieRating r
    JOIN Movies m ON m.movie_id = r.movie_id
    WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY r.movie_id, m.title
)
(
    SELECT 
        name AS results
    FROM cte
    ORDER BY cnt DESC, name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT 
        title AS results
    FROM cte2
    ORDER BY avr DESC, title ASC
    LIMIT 1
);
