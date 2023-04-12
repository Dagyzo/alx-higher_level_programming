#!/usr/bin/python3
"""Defines a class rectangle that inherits from BaseGeometry."""
BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(Basegeometry):
    """REpresents a rectangle using BaseGeometry."""

    def _init_(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            Height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
