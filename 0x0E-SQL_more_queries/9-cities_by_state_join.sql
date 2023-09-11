-- lists all cities contained in the database hbtn_0d_usa
-- echo 'SELECT * FROM states;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- cat 9-cities_by_state_join.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa

SELECT c.id, c.name, s.name
FROM cities c
JOIN states s ON c.state_id = s.id
ORDER BY c.id ASC;

-- (SELECT name FROM states WHERE id = cities.state_id) AS ""
