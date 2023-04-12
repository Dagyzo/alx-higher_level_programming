#!/usr/bin/python3
"""
Defines a rectangle class that inherits from BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with an explanation message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a given value if it is a positive integer

        Args:
            name (str): the name string
            value (int): the value to validate

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize a new Rectangle instance

        Args:
            width (int): width of the rectangle, must be a positive integer
            height (int): height of the rectangle, must be a positive integer
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
