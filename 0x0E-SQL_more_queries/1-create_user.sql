--This script will be creating a user called user_0d_1
--the user password should be set to user_od_1_pwd
--if the user already exist the script shouldn't fail

CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
