#!/usr/bin/python3
"""Module to change the name of Arizona state at id = 2 to New mexico state in
mysql database using SQLAlchemy """

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
    state = session.query(State).filter_by(id=2).first()

    """Update the name of the state id = 2 to 'New Mexico'"""
    state.name = "New Mexico"

    """Commit the session.
    This is to persist the changes"""
    session.commit()
