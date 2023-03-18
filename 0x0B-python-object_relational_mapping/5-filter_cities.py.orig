<<<<<<< HEAD
5-filter_cities.py
=======
#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
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

    cur.execute("SELECT name FROM cities\
                    WHERE state_id =\
                        (SELECT id FROM states WHERE name = %(name)s)\
                            ORDER BY cities.id ASC", {'name': state})

    if rows := cur.fetchall():
        print(", ".join([record[0] for record in rows]))

    cur.close()
    db.close()
>>>>>>> 8db4a942f6188b86fa6a63a117697dd2a1003f02
