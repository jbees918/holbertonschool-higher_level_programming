#!/usr/bin/python3
"""
script to list all states from the database hbtn_0e_0_usa
"""
import MySQLdb


def print_states():
    """
    Prints all states from the database hbtn_0e_0_usa
    """
    from sys import argv
    db = MySQLdb.Connect(host="localhost", port=3306, user=argv[1], passwd=argv[2]), database=argv[3])

    cur = db.curser()

    cur.execute("SELECT * FROM states")
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    print_states()
