-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- cat 13-count_shows_by_genre.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
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
