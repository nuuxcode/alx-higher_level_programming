-- creates the table force_name
-- cat 3-force_name.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'SELECT * FROM force_name;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO force_name (id) VALUES (333);' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);

