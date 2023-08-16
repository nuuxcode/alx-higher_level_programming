-- lists all Comedy shows in the database hbtn_0d_tvshows
-- cat 15-comedy_only.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT s.title AS title
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY title ASC;
