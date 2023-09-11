-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- cat 6-states.sql | sudo mysql -hlocalhost -uroot -p
-- echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
-- echo 'SELECT * FROM states;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE
    IF NOT EXISTS states (
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY UNIQUE,
        name VARCHAR(256)
    )
