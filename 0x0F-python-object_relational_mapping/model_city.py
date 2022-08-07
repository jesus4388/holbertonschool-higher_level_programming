#!/usr/bin/python3
'# class definition of a  city'

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '# contains the class definition of a City'

    __tablename__ = 'cities'
    __table_args__ = {
            'mysql_engine': 'InnoDB',
            'mysql_default_charset': 'latin1'
            }
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
