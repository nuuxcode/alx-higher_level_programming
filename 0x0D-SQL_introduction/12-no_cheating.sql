-- updates the score of Bob to 10 in the table second_table
-- cat 12-no_cheating.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
UPDATE second_table
SET score = 10
WHERE name = "Bob";
