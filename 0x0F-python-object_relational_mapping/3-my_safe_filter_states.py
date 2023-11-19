#!/usr/bin/python3
"""Module to list all states from sql db"""
import sys
import MySQLdb

if __name__ == '__main__':

    """Get commandline args."""
    username = sys.argv[1]
    password = sys.argv[2]
    sqlDb = sys.argv[3]
    stateName = sys.argv[4]

    """Use variables set as mysql credentials to connect to mysql server
       search name from command line arguments
       """
    conn = MySQLdb.connect(user=username, passwd=password, db=sqlDb)
    cur = conn.cursor()

    """SQL query with placeholders"""
    sql_query = "SELECT * FROM states WHERE `name` = %s"

    """Execute above prepared query"""
    cur.execute(sql_query, (stateName,))

    """Printing the data filtering the specified state name"""
    for state in cur.fetchall():
        print(state)
