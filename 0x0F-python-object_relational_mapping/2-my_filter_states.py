#!/usr/bin/python3
"""Module to list all states from sql db"""
import sys
import MySQLdb

if __name__ == '__main__':
    """Use mysql credentials to connect to mysql server
       search name from command line arguments
       """
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()

    """Sql query to fetch state as specified in argument[4]"""
    cur.execute("SELECT * FROM states WHERE `name` = '{}'".format(sys.argv[4]))

    """Printing the data filtering the specified state name"""
    for state in cur.fetchall():
        print(state)
