#!/usr/bin/python3
'# a script that deletes all State objects with a name'

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    for i in session.query(State).all():
        for x in i.name:
            if x == 'a' or x == 'A':
                session.delete(i)

    session.commit()
    session.close()
