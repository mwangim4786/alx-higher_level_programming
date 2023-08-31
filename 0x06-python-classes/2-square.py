#!/usr/bin/python3
""" Module to define class Square """


class Square:
    """ Square with private attribute size """

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
        