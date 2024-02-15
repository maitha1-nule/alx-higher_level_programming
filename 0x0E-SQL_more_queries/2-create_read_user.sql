--A script that creted a database hbtn_0d_2 and the user user_0d_2.
--then set the password of the user to user_0d_2_pwd
--and finally if the db exusts the querry should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED WITH 'user_0d_2_pwd';
GRANT USER SELECT ON  hbtn_0d_2.* TO 'user_0d_2'@'localhost';
