-- get all cities of california , by selecteing
-- all cities with state id(fk) corresponding to california
-- Data Manipulation Language (DML) query, because it filters and ordering the result
SELECT id,name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = 'California')
 ORDER BY cities.id ASC;
