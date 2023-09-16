#!/usr/bin/python3
""" task 4 : py script to get all cities from
user selected database
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    DB_CONFIG = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "passwd": argv[2],
        "db": argv[3],
        "charset": "utf8",
    }

    db_connection = MySQLdb.connect(**DB_CONFIG)
    cur = db_connection.cursor()
    try:
        sql_cmd = """
        SELECT cities.id, cities.name, states.name
        FROM cities, states
        WHERE cities.state_id = states.id
        ORDER BY cities.id ASC;
        """
        cur.execute(sql_cmd)
        result = cur.fetchall()

        for record in result:
            print(record)

    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))

    cur.close()
    db_connection.close()
