#!/usr/bin/python3
""" script that lists all states from the database
with a name starting with N (upper N)"""
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
        SELECT * FROM states
        WHERE name LIKE BINARY '{:s}'
        ORDER BY id ASC;
        """.format(
            argv[4]
        )

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
