#!/usr/bin/python3
"""
task 11: python boilerplate script to ADD RECORD to database
using sqlalchemy orm
"""
from sys import argv

# import models
from model_state import Base, State

# import sqlalchemy tools to work with
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    # configure sqlalchemy create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )

    # create session
    # # First, create an instance of sqlalchemy sessionmaker class
    session_maker = sessionmaker()
    # Configure sessionmaker to use specified database engine
    session_maker.configure(bind=engine)
    # Create a session instance from configured session_maker
    session = session_maker()

    new_state = State(name="Louisiana")

    # this only places instances in the session you need to commit or
    # flush to actually push it
    session.add(new_state)

    # add record(row) to the table
    session.commit()

    # this is just task related requirement
    print(new_state.id)

    # Don't forget to close session
    session.close()
