#!/usr/bin/python3
"""Module to list all states from sql database = """
import sys
import MySQLdb

if __name__ == '__main__':

    """Connect to mysql server using commandline arguments"""
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """Connect to sql server"""
    cur = conn.cursor()

    """Excecute SQL query to fetch all cities by state"""
    query = ("SELECT * FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.`id` \
                 ORDER BY `c`.`id`")

    cur.execute(query)

    # Fetch all the rows of data from table
    query_rows = cur.fetchall()

    # Printing the data
    for city in query_rows:
        if city[4] == sys.argv[4]:
            x = ", ".join([city[2]])
            print(x)
