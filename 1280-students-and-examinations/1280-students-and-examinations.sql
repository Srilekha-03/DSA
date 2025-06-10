# Write your MySQL query statement below
WITH cte AS (
  SELECT *
  FROM Students
  CROSS JOIN Subjects
),
cte2 AS (
  SELECT student_id, subject_name,
         COUNT(subject_name) AS count
  FROM Examinations
  GROUP BY student_id, subject_name
)
SELECT cte.student_id,
       cte.student_name,
       cte.subject_name,
       CASE 
           WHEN count IS NOT NULL THEN count
           ELSE 0
       END AS attended_exams
FROM cte
LEFT JOIN cte2
  ON cte.student_id = cte2.student_id
 AND cte.subject_name = cte2.subject_name
ORDER BY cte.student_id, cte.subject_name
