--a script that creates the table unique_id on your MySQL server.
--atr1:int
--atr2:VARCHAR(256)
--return no error ven if table a

CREATE TABLE IF NOT EXISTS 'unique_id'(id INT DEFAULT 1 UNIQUE, 'name' VARCHAR(256) );
