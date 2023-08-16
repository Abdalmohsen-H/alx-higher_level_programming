-- task 11 : script for selecting TV shows and their genres, in specific order
-- but also include all titles even if they don't have geners(i.e. not in geners table)
-- so use left join where table a for titles , and table for geners
-- Data Manipulation Language (DML) query, because ordering the result
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
