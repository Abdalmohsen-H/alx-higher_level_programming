#!/usr/bin/python3
"""
task 14: Model, python file for city model class ,
also import proviusly createed instance Base = declarative_base()
from state_model.py
that City class will inherit from
this is just a basic examble to create a model
ref : https://docs.sqlalchemy.org/en/13/orm/
        extensions/declarative/basic_use.html
"""
from sqlalchemy import Column, Integer, String
from model_state import Base



class City(Base):
    """Class for City Model to define cities table"""

    __tablename__ = "cities"
    id = Column(
        Integer, primary_key=True, nullable=False,
        autoincrement=True, unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(state.id), nullable=False)
