#!/usr/bin/python3
""" script that lists all states """
import MySQLdb
import sys
if __name__ =="__main__":
  db =  MySQLdb.connect("localhost",user = sys.argv[1],password = sys.argv[2], db = sys.argv[3], port=3306)
  c = db.cursor()
  c.execute("SELECT * FROM states")
  rows = c.fetchall()
  for row in rows:
    print(row)
  c.close()
  db.close()
