#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="BinaryKid",
        db="hbtn_0e_0_usa"
        )
cur = db.cursor()
cur.execute("SELECT states FROM hbtn_0e_0_usa")
cur.close()
db.close()
