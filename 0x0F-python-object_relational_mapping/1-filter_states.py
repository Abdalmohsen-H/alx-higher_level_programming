#!/usr/bin/python3
""" script that lists all states from the database
with a name starting with N (upper N)"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8")
    cur = db_connection.cursor()
    try:
        sql_cmd = """
        SELECT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY id ASC
        """
        cur.execute(sql_cmd)
        result = cur.fetchall()
        for record in result:
            print(record)
    except MySQLdb.Error:
        try:
            print(f"MySQL Error [{e.args[0]}]: {e.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(e)}")

    cur.close()
    db_connection.close()
