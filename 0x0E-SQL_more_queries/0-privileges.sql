-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 
-- cat 0-privileges.sql | sudo mysql -hlocalhost -uroot -p
-- echo "CREATE USER 'user_0d_1'@'localhost';" |  sudo mysql -hlocalhost -uroot -p
-- echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  sudo mysql -hlocalhost -uroot -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
