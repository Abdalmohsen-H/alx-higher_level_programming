-- task 4 : script to Create a table 'id_not_null'
-- while setting is cloumn's Default to 1
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id` INT DEFAULT 1,
    `name` VARCHAR(256)
);
