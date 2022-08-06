#!/usr/bin/python3
'a python file that contains the class definition of a State'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Table

Base = declarative_base()

class State(Base):

    __tablename__ = 'states'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_default_charset': 'latin1'}
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
