-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- cat 14-my_genres.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT g.name AS name
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY name ASC;
