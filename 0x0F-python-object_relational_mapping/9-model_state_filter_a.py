#!/usr/bin/python3
"""Module to retrieve and print states with letter 'a' from mysql database using SQLAlchemy """

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
    al_query = session.query(State).order_by(State.id)

    for state in al_query:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
