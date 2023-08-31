#!/usr/bin/python3
""" Module to define class Square with private instance 
attribute: size """


class Square:
    """ Square with private attribute size set to 0 """

    def __init__(self, size=0):
        """
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.size = size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """

        return self.__sizeof__
    
    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        
        if type(value) is int:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')
        

    def area(self):
        """
        calculates area of square
        Returns:
            the area of the square
        """

        return self.__size * self.__size