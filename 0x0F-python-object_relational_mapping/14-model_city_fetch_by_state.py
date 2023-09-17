#!/usr/bin/python3
"""
task 14 fetch: this task select all records from two table
to print  all City objects in specific format
<state name>: (<city id>) <city name>
python boilerplate script to query database using sqlalchemy orm
"""
import sys

# import models
from model_state import Base, State
from model_city import City

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

    # don't forget ( ) to have multiline
    query_result_list = (
        session.query(State.name, City.id, City.name)
        .join(State, State.id == City.state_id)
        .order_by(asc(City.id))
        .all()
    )

    # or like below
    # query_res = session.query(State.name, City.id, City.name).\
    #    join(City, State.id == City.state_id).order_by(City.id).\
    #    all()

    for res_row_set in query_result_list:
        # unpacking the row set
        print("{:s}: ({:d}) {:s}".format(*res_row_set))

    # Don't forget to close session
    session.close()
