#!/usr/bin/python3
""" task 2 : py script that lists filter states by user input
BTW this task's code isn't blocking SQL injec-tion

for example : this is SQL inje-ction to get all results instead
./2*py username pwd db_name "' OR '1'='1' --'"

this will be solved on the next task; task 3
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
