#!/bin/usr/python3
"""
Script to list all cities from 
the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def print_cities_states():
    """
    method for listing all cities from sql table
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states\
                WHERE cities.state_id = states.is\
                ORDER BY cities.id")
    
    for row in cur.fetchall():
        print(row)

    cur.close()
    cur.db()


    if __name__ == "__main__":
        print_cities_states()
