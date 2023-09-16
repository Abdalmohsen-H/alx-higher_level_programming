#!/usr/bin/python3
"""
    task 6: Model, python file for state model class ,
    also create instance Base = declarative_base()
    that state class will inherit from
    this is just a basic examble to create a model
    ref : https://docs.sqlalchemy.org/en/13/orm/
          extensions/declarative/basic_use.html
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class"""

    __tablename__ = "states"
    id = Column(
        Integer, primary_key=True, nullable=False,
        autoincrement=True, unique=True
    )
    name = Column(String(128), nullable=False)
