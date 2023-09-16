#!/usr/bin/python3
""" script that lists all citiess """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON\
             cities.state_id = states.id ORDER BY cities.id")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
