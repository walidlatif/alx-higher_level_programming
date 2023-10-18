--Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
    c.name AS genre,
    COUNT(*) AS number_of_shows
FROM
    tv_genres c
    JOIN tv_show_genres s ON c.id = s.genre_id
GROUP BY
    c.name
ORDER BY
    number_of_shows DESC;
