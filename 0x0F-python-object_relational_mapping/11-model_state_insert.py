#!/usr/bin/python3
"""Module to add a new state to mysql database using SQLAlchemy """

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

    """Create a new state object for Louisiana state"""
    louisiana = State(name="Louisiana")

    """Add the new state to the session"""
    session.add(louisiana)

    """Commit the session.
    This is to persist the changes"""
    session.commit()


    """Print ID of the added state"""
    print(louisiana.id)
