-- task 1: create user for MySQL server, user_0d_1, with pwd user_0d_1_pwd
-- then give him all permissions(PRIVILEGES)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
