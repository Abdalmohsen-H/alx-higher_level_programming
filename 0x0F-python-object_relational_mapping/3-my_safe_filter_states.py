#!/usr/bin/python3
""" task 3 : py script to reduce SQL inj-ections attacks
when this scipt tryies to filter states by user input
to solve issues with task 2

solution is Parameterized queries to cur.excute directly
this will ensure that user's input is properly sanitized &
separated from the SQL query,
this way ensures that user's input is treated as data &
not as executable code which reduces the risk of SQL injection.

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
        user_input = argv[4]
        sql_cmd = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC;
        """
        # cur.excute's 2nd argument must be a tuple of values.
        cur.execute(sql_cmd, (user_input, ))
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
