#!/usr/bin/python3
'# a script that lists all cities from the database hbtn_0e_4_usa'

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    db_conection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            db=argv[3])
    cursor = db_conection.cursor()
    cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities JOIN states "
            "ON cities.state_id = states.id "
            "ORDER BY cities.id")
    resultado = cursor.fetchall()

    for x in resultado:
        print(x)

    cursor.close()
    db_conection.close()
