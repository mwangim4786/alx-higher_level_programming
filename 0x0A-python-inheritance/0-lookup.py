#!/usr/bin/python3
"""
Contains the lookup function
"""


def lookup(obj):
    """function that returns a list of available attributes and methods of an object"""
    return dir(obj)