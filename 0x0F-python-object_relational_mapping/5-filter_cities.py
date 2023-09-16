#!/usr/bin/python3
""" task 5 : py script to get cities of a state when
user input select an existing state
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
        SELECT cities.name
        FROM cities
        WHERE cities.state_id = (
            SELECT states.id FROM states
            WHERE states.name = %s
            )
        ORDER BY cities.id ASC;
        """
        # cur.excute's 2nd argument must be a tuple of values.
        cur.execute(sql_cmd, (user_input,))
        result = cur.fetchall()

        # 1st solution
        # for idx, record in enumerate(result):
        #     if (idx < (len(result) - 1)):
        #         print(record[0], end=", ")
        #     else:
        #         print(record[0])

        # another solution is to loop and save to list
        # then create string from list with join using comma
        # then print this string
        cities_list = []
        for record in result:
            cities_list.append(record[0])
        print(", ".join(cities_list))

    except MySQLdb.Error as e:
        try:
            print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        except IndexError:
            print("MySQL Error: {}".format(str(e)))

    cur.close()
    db_connection.close()
