--  task 14: script to show all genres for tv show dexter
-- only the geners displayed in specific order
SELECT
  tv_genres.name AS name
  FROM tv_show_genres
  INNER JOIN tv_genres
  ON tv_show_genres.genre_id = tv_genres.id
  INNER JOIN tv_shows
  ON tv_shows.id = tv_show_genres.show_id
  AND tv_shows.title = 'Dexter'
  ORDER BY name;
