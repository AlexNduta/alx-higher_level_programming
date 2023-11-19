#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    try:
        # Connect to the database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )

        # Create a cursor to execute queries using SQL;
        cursor = db.cursor()
        sql_cmd = """SELECT *
                        FROM states
                        WHERE name LIKE '{:s}'
                        ORDER BY id ASC""".format(argv[4])
        cursor.execute(sql_cmd)

        # Fetch and process the results
        for row in cursor.fetchall():
            if row[1] == argv[4]:
                print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        cursor.close()
        db.close()
