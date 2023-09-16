#!/usr/bin/python3
""" script that lists all citiess """
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect("localhost", user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM\
            cities INNER JOIN states ON cities.state_id = states.id")
    rows = c.fetchall()
    print(", ".join([rr[2] for rr in rows if rr[4] == sys.argv[4]]))
    c.close()
    db.close()
