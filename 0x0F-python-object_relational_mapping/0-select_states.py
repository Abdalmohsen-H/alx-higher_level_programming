#!/usr/bin/python3
""" python code to lists all states records
from database named hbtn_0e_0_usa using MySQLdb"""
from sys import argv
import MySQLdb
if __name__ == "__main__":
    # connection data
    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3],
        charset="utf8")
    cur = conn.cursor()
    try:
        myquery = "SELECT * FROM states ORDER BY id ASC"
        cur.execute(myquery)
        result = cur.fetchall()
    except Exception as e:
        print(f"Error : {e}")

    for record in result:
        print(record)
    cur.close()
    conn.close()
