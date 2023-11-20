#!/usr/bin/python3
"""Module to print state object from a search in mysql database using SQLAlchemy """

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

    """Search for the specified state in yhe database and print it else 
    print not found"""
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True

    """Message to be printed if object if not found"""
    if found is False:
        print("Not found")
