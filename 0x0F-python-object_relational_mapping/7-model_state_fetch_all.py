#!/usr/bin/python3
' a script that lists all State objects from the database hbtn_0e_6_usa'

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)

    for i in session.query(State).order_by(State.id).all():
        print("{}: {}".format(i.id, i.name))
    session.close()
