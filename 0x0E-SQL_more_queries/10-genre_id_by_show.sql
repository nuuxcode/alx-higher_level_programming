-- Import the database dump from hbtn_0d_tvshows
-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- cat 10-genre_id_by_show.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows

SELECT c.title, s.genre_id
FROM tv_shows c
JOIN tv_show_genres s ON c.id = s.show_id
ORDER BY c.title, s.genre_id ASC;
