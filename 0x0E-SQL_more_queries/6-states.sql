-- Task 6 : script that Creates database hbtn_0d_usa with table states
-- id is pk, auto generated , can't be null
-- name can't be Null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);
