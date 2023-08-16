-- task 5 : Create table unique_id , while setting
-- id cloumn's Default to 1 and uinque 
CREATE TABLE IF NOT EXISTS `unique_id` (
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);
