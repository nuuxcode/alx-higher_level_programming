--  lists all shows contained in the database hbtn_0d_tvshows
-- cat 11-genre_id_all_shows.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT c.title, s.genre_id
FROM tv_shows c
LEFT JOIN tv_show_genres s ON c.id = s.show_id
ORDER BY c.title, s.genre_id ASC;
