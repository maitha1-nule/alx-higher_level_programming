--a  query that creates a DB table with 2 attributes
--Atr1:int
--attr2:var(256)
--return no error even if it exists

CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'states'('id' INT AUTO_INCREMENT PRIMARY KEY, 'name' VARCHAR(256) NOT NULL;
--
