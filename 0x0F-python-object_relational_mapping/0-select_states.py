#!/usr/bin/python3
'# script that lists all states from the database hbtn_0e_0_usa'

if __name__ == '__main__':

    from sys import argv
    import MySQLdb

    db_connection = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3]
            )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    cursor.close()
    db_connection.close()
