#!/usr/bin/python3
' a script that lists all State objects from the database hbtn_0e_6_usa'

from sqlalchemy import create_engine
from sqlalchemy.orm sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
