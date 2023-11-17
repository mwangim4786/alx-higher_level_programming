#!/usr/bin/python3
"""Module to list all states from sql db"""
import sys
import MySQLdb

def list_states(username, password, database):

    # Connect to mysql server
    conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = conn.cursor()

    # Sql query to fetch all states
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows of data from table
    query_rows = cur.fetchall()

    # Printing the data
    for row in query_rows:
        print(row)

    # Close database connection
    cur.close()
    conn.close()

# How it is utilised
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
