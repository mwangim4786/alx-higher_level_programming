#!/usr/bin/python3
""" Module to define class Square """


class Square:
    """ Representation of a Square 
    
    Attribures:
    __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size