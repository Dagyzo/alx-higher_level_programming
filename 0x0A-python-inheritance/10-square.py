#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""


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
        """Initializes a Rectangle instance

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        super().__init__()
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """Computes the area of a Rectangle instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes a Square instance

        Args:
            size (int): the size of the square
        """
        super().__init__(size, size)
        self.__size = self.integer_validator("size", size)

    def __str__(self):
        """Returns a string representation of a Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)
