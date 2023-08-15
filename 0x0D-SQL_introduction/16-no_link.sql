-- lists all records of the table second_table
-- cat 16-no_link.sql | sudo mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT
    score,
    name
FROM
    second_table
WHERE
    name IS NOT NULL
ORDER BY
    score DESC;
