--A script that creates a table named second_table
--in the databse hbtn_0c_c


CREATE TABLE IF NOT EXISTS 'second_table'( 'id' INT, 'name' VARCHAR(256), 'score' INT);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES(1,  'John', 'score' = 10);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES(2,  'Alex', 'score' = 3);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES(3,  'Bob', 'score' = 14);
INSERT INTO 'second_table' ('id', 'name', 'score') VALUES(4,  'George', 'score' = 8);
