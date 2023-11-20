#!/usr/bin/python3
"""Module to delete all states containing letter 'a' from the mysql database using SQLAlchemy """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    """Retrieve cities and their respective states from the database"""
    state_query = session.query(City, State).filter(City.state_id == State.id) .order_by(City.id)

    for city, state in state_query:
        """Print state and  city info."""
        print("{}: ({}) {}".format(state.name, city.id, city.name))
