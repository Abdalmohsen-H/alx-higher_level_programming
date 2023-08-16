-- task2 : A.Hesham - SQL commands to Create database hbtn_0d_2
-- Also user user_0d_2 with pwd give hime SELECT privilege on hbtn_0d_2
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
