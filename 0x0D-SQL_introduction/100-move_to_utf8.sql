-- task 17: convert(alter) database and tables to specific setting like char set and collate
-- first select database
USE hbtn_0c_0;
-- then alter character set and collate
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
