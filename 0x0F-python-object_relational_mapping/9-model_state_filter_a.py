#!/usr/bin/python3
"""
task 9: python boilerplate script to query database using sqlalchemy orm
this task select all records from a table with state.name contains a letter
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

    query_result_list = (
        session.query(State)
        .filter(State.name.like("%a%"))
        .order_by(asc(State.id))
        .all()
    )

    for city_record in query_result_list:
        print(f"{city_record.id}: {city_record.name}")

    # Don't forget to close session
    session.close()
