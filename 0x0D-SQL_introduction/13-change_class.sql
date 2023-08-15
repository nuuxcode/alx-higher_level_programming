-- removes all records with a score <= 5 in the table second_table
-- cat 13-change_class.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
DELETE FROM second_table
WHERE score <= 5;
