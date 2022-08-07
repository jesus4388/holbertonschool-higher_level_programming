#!/usr/bin/python3
'# a script that deletes all State objects with a name'

from sqlalchemy.orm import Session
from sqlalchemy import create_engine, update
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    session.query(State).filter(State.name.contains('a%')).delete(
            synchronize_session='fetch')
    session.commit()
    session.close()
