#!/usr/bin/python3
'# script that takes in an argument and displays all values in the states'

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
    a = argv[4]
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id".format(a))
    resultado = cur.fetchall()

    for i in resultado:
        print("{}".format(i))

    db_conection.close
    cur.close
