#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base



class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character to stdout."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        
        for h in range(self.height):
            for w in range(self.width):
                print("#", end="")
            print("")  


    def __str__(self):
        return "[Rectangle]" str(self.id) str(self.x)+"/"+str(self.y) str(self.width)+"/"+str(self.height)


