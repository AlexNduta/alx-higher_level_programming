#!/usr/bin/python3
"""
Takes an argument and displays all values in the `states`ntable of `hbtn_0e_0_usa` where `name` matches the argument
"""

#import necesary modules
import MySQLdb
from sys import argv
if __name__ == "__main__":
    try:
        # creaate a connector
        db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3],
                name= input(argv[4])
                )
        # create a cursor
        cur = db. cursor()

        # start executing statements
        cur.execute("SELECT * FROM state WHERE name='%s' ORDER BY id ASC;", (name))
        for row  in cur.fetchall():
            print(row)
    except:
        print("Error")

    finally:
        cur.close()
        db.close()


