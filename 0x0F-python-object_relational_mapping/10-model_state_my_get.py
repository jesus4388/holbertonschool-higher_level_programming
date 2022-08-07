#!/usr/bin/python3
'# a script that prints the State object with the name'

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    for i in session.query(State).where(State.name == argv[4]).order_by(
            State.id).all():
        try:
            print(i.id)
        except Exception:
            print("Not found")

    session.close()
