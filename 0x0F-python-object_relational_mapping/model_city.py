#!/usr/bin/python3
"""Defines the city model.
Inherits from SQLAlchemy Base and links to the MySQL table cities"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents the city table in MYSQL database.

    __tablename__ (str): Name of mysql table.
    Attributes:
        id (str): The city's id.
        name (sqlalchemy.Integer): City's name.
        state_id (sqlalchemy.String): City's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
