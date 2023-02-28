#!/bin/urs/python3
"""
this script takes in the name of a state as an arg
and lists all the cities in that state, with the database 
hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])

cur = db.cursor()
state = sys.argv[4]

