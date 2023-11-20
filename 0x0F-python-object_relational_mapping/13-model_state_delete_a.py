#!/usr/bin/python3
"""Module to delete all states containing letter 'a' from the mysql database using SQLAlchemy """

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

    """Retrieve state with id = 2 from the database"""
    state_query = session.query(State)

    for state in state_query:
        """Check if state name contains letter 'a'"""
        if "a" in state.name:
            """Delete the state from the database"""
            session.delete(state)

    """Commit the session.
    This is to persist the changes"""
    session.commit()
