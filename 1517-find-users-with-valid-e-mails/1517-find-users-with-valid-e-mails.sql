# Write your MySQL query statement below
SELECT *
FROM Users
WHERE 
    mail LIKE '%@leetcode.com'                  -- domain check (case-sensitive)
    AND mail NOT LIKE '%@LEETCODE.COM%'        -- exclude uppercase variants
    AND mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$';
