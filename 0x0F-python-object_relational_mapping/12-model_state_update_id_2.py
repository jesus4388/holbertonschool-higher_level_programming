#!/usr/bin/python3
'# a script that changes the name of a State object'

from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import update
from model_state import Base, State
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    index = 2
    session = Session(engine)
    for i in session.query(State).filter(State.id == 2):
        i.name = "New Mexico"

    session.commit()
    session.close()
