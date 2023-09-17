#!/usr/bin/python3
"""
task 12: python boilerplate script to query database using sqlalchemy orm
this task update one record on a table
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

    query_res_list = session.query(State).filter(State.id == 2)

    for city_record in query_res_list:
        # change record.name
        city_record.name = "New Mexico"

    # commit record(row) update to the table
    session.commit()

    # Don't forget to close session
    session.close()
