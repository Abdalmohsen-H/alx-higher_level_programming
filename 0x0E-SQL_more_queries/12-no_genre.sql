-- task 12 : script for  lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- in specific order
-- but also include all titles even if they don't have geners(i.e. not in geners table)
-- so use left join where table a for titles , and table for geners
-- Data Manipulation Language (DML) query, because filtering and ordering the result
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows LEFT JOIN tv_show_genres
  ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_show_genres.show_id IS NULL
  ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
