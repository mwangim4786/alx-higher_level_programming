#!/usr/bin/python3
"""Module to retrieve and print the first state from mysql database using SQLAlchemy """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """Create SQLAlchemy engine using the credentials from the
        commandline arguments.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping=True)

    """Create session"""
    Session = sessionmaker(bind=engine)

    """Create a session object"""
    session = Session()

    """Print all states' id's and names from the database"""
    state = session.query(State).order_by(State.id).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
