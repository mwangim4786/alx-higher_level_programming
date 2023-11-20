#!/usr/bin/python3
"""Module to to define the state class representing a state table in the database """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Represents the state table in MYSQL database.
    __tablename__ (str): Name of mysql table.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): State name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
