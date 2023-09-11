-- computes the score average of all records in the table second_table
-- cat 14-average.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT AVG(score) AS average
FROM second_table;
