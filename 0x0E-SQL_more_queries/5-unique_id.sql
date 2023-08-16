-- creates the table unique_id
-- cat 5-unique_id.sql | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'SELECT * FROM unique_id;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
-- echo 'SELECT * FROM unique_id;' | sudo mysql -hlocalhost -uroot -p hbtn_0d_2
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256))
