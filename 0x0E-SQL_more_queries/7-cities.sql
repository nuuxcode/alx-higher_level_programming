-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) 
-- cat 7-cities.sql | sudo mysql -hlocalhost -uroot -p
-- echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM cities;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa
CREATE TABLE
    IF NOT EXISTS cities (
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
        state_id INT NOT NULL,
        name VARCHAR(256) NOT NULL,
        FOREIGN KEY (state_id) REFERENCES states (id)
    )
