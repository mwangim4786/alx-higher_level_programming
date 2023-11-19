#!/usr/bin/python3
"""Module to list all states from sql db"""
import sys
import MySQLdb

if __name__ == '__main__':
    """Connect to mysql server"""
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    """Sql query to fetch state as specified in argument[4]"""
    cur.execute("SELECT * FROM states WHERE `name` = '{}'".format(sys.argv[4]))

    # Printing the data
    for state in cur.fetchall():
        print(state)
