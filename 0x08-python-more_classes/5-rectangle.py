#!/usr/bin/python3
"""
This module defines the Rectangle class
"""


class Rectangle:
    """
    Rectangle class with width and height attributes
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the given width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of this Rectangle instance
        """
        return self.width * self.height

    def perimeter(self):
        """
        Computes the perimeter of this Rectangle instance
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of this Rectangle instance
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        Returns a string representation of this Rectangle instance
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        Prints a message when this Rectangle instance is deleted
        """
        print("Bye rectangle...")
