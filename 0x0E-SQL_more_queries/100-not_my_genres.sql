-- task 100: script to show all genres that not a genere for tv show dexter
-- only the geners displayed in specific order
SELECT DISTINCT `name`
  FROM `tv_genres` AS tvgen
       INNER JOIN `tv_show_genres` AS tsg
       ON tvgen.`id` = tsg.`genre_id`

       INNER JOIN `tv_shows` AS tv
       ON tsg.`show_id` = tv.`id`
       WHERE tvgen.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS tvgen
	             INNER JOIN `tv_show_genres` AS tsg
		     ON tvgen.`id` = tsg.`genre_id`

		     INNER JOIN `tv_shows` AS tv
		     ON tsg.`show_id` = tv.`id`
		     WHERE tv.`title` = "Dexter")
 ORDER BY tvgen.`name`;
