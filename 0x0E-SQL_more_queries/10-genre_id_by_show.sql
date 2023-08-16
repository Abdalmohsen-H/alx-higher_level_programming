-- task 10 : script for selecting TV shows and their genres, in specific order
-- Data Manipulation Language (DML) query, because ordering the result
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows INNER JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
