#!/usr/bin/python3
"""Module to list all states from sql db"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Connect to mysql server
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    # Sql query to fetch all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Printing the data retrieving all states starting with 'N'
    for state in cur.fetchall():
        if state[1][0] == "N":
            print(state)
