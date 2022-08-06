#!/usr/bin/python3
'# Script that lists all states with a name starting with N'

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_conection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3]
            )
    cur = db_conection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    resultado = cur.fetchall()

    for x in resultado:
        print(x)

    cur.close()
    db_conection.close()
