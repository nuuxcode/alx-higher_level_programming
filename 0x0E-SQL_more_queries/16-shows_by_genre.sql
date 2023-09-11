-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
-- cat 16-shows_by_genre.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT
    s.title AS title,
    g.name AS name
FROM
    tv_shows s
    LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
    LEFT JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY
    title,
    name ASC;
