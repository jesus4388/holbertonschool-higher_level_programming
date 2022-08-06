#!/usr/bin/python3
'# a script that takes in the name of a state as an argument'

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
    arg = argv[4]
    cursor.execute(
            "SELECT cities.name "
            "FROM cities JOIN states "
            "ON cities.state_id=states.id "
            "WHERE states.name=%s", (arg,))
    resultado = cursor.fetchall()

    stdo = ""
    b = 0
    for i in resultado:
        if len(resultado) - 1 != b:
            stdo += i[0] + ", "
        else:
            stdo += i[0]
        b += 1
    print(stdo)

    cursor.close()
    db_conection.close()
