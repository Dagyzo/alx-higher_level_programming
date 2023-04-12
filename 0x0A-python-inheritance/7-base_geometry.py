#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


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
