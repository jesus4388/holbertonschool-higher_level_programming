#!/usr/bin/python3
'# a script that is safe from MySQL injections'

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_conection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3])
    cur = db_conection.cursor()
    arg = argv[4]
    cur.execute("SELECT * FROM states WHERE name=%s", (arg,))
    resultado = cur.fetchall()

    for i in resultado:
        print(i)

    cur.close()
    db_conection.close()
