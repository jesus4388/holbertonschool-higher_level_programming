#!/usr/bin/python3
'# a script that prints the first State object from the database hbtn_0e_6_usa'

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    session = Session(engine)
    for i in session.query(State).order_by(State.id).all():
        print("{}: {}".format(i.id, i.name))
        break;

    session.close()
