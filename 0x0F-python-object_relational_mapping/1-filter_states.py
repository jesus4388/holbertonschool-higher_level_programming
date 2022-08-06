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
    cursor = db_conection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    cursor.close()
    db_conection.close()
