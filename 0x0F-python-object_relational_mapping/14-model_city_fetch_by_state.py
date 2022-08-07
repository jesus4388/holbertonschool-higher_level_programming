#!/usr/bin/python3
'# script that prints all'

from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    for i, b in session.query(City, State).filter(
            City.state_id == State.id).order_by(State.id):
        print("{}: ({}) {}".format(b.name, i.id, i.name))

    session.commit()
    session.close()
