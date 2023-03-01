#!/usr/bin/python3
'''Get All States, requires User, Password, Database'''
import MySQLdb
import sys


def get_all_states():
    '''Get States from sql table'''
    if(len(sys.argv) < 4):
        print(sys.argv)
        return
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    try:
        db = MySQLdb.connect(
            "localhost",
            mysql_username,
            mysql_password,
            database_name)
    except Exception as e:
        return (0)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()


if __name__ == '__main__':
    get_all_states()
