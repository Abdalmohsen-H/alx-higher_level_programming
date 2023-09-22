#!/usr/bin/python3
"""
task 100: python boilerplate script to ADD RECORDs to database
while states table relation with other table cities
 creates the State “California” with the City “San Francisco”
using sqlalchemy orm
this task select all records from a table
"""
import sys

# import models
from model_state import Base, State

# import sqlalchemy tools to work with
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import asc

if __name__ == "__main__":
    # configure sqlalchemy create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # create session
    # # First, create an instance of sqlalchemy sessionmaker class
    session_maker = sessionmaker()
    # Configure sessionmaker to use specified database engine
    session_maker.configure(bind=engine)
    # Create a session instance from configured session_maker
    session = session_maker()

    nw_sta_name = "California"
    nw_cty_name = "San Francisco"
    nw_state = State(name=nw_sta_name)
    new_city = City(name=nw_cty_name)
    new_state.cities.append(new_city)
    session.add(new_state)

    # add records
    session.commit()

    # Don't forget to close session
    session.close()
