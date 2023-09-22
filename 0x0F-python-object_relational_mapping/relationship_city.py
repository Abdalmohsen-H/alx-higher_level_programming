#!/usr/bin/python3
"""
task 100: city Model with relation to state,
python file for city model class ,
also import proviusly createed instance Base = declarative_base()
from relationship_state.py
that City class will inherit from
this is just a basic examble to create a model
ref : https://docs.sqlalchemy.org/en/13/orm/
        extensions/declarative/basic_use.html
it's like task 14 but how the relation is new here
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class for City Model to define cities table"""

    __tablename__ = "cities"
    id = Column(
        Integer, primary_key=True, nullable=False,
        autoincrement=True, unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
