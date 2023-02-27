#!/usr/bin/python3
"""
This script takes arguments and displays all the values 
in the states table of hbtn_0e_0_usa where name matches
arg, while being safe from mySQL injections
"""
import MySQLdb
import sys


def print_state_id():
    db = MySQLdb.connect(host='localhost',
                         port=3306, 
                         user=sys.argv[1]
                         passwd=sys.argv[2]
                         database=sys.argv[3])
    cur = db.curcor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s\
                ORDER BY id", (sys.argv[4]))
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


    if __name__ == "__main__":
        print_state_id()
