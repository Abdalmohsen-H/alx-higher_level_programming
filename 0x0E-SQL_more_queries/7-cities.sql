-- task 7: create a script that create a database and table
-- also set relation between two tables using foreign key
-- using DDL query
-- first create the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- command to move to database to use it
USE hbtn_0d_usa;
-- create table in the above database if doesnt exists
-- and set pk and fk
CREATE TABLE IF NOT EXISTS cities(
  id INT NOT NULL AUTO_INCREMENT UNIQUE,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (state_id) REFERENCES states(id)
);
