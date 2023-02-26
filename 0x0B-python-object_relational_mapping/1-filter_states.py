#!/usr/bin/python3
"""
This script lists all states with name starting
with N (uppercase N) from database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


def print_stateN():
    """
        Print the states from the database
    """
    db = MySQLdb.connect(host='localhost', 
                         port=3306,
                         user=sys.argv[1],
                         paswd=sys.argv[2],
                         database=sys.argv[3])
    cur.dbcursor()
    cur.execute("SESECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY states.id ASC;")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_stateN()
