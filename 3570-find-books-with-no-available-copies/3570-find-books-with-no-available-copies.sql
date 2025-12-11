# Write your MySQL query statement below
SELECT 
    b.book_id,
    b.title,
    b.author,
    b.genre,
    b.publication_year,
    COUNT(r.record_id) AS current_borrowers
FROM library_books b
LEFT JOIN borrowing_records r
    ON b.book_id = r.book_id AND r.return_date IS NULL
GROUP BY 
    b.book_id, b.title, b.author, b.genre, b.publication_year,b.total_copies
HAVING COUNT(r.record_id) = b.total_copies
ORDER BY current_borrowers DESC, b.title ASC;