--  task 13: script for  show genres and count of shows linked to it
-- only show geners that have shows, order result by number of shows
-- Data Manipulation Language (DML) query, because of ordering the result
SELECT
  tv_genres.name AS genre,
  COUNT(tv_show_genres.genre_id) AS number_of_shows
  FROM tv_show_genres
  INNER JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
  GROUP BY genre
  ORDER BY number_of_shows DESC;
