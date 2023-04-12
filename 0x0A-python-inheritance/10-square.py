#!/usr/bin/python3
"""DEfines a Rectangle subclass square."""
Rectangle = _import_('9-rectangle').Rectangle


class square(Rectangle):
    """Represents a square."""

    def _init_(self, size):
        """Initialize a new square

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super()._init_(size, size)
        self._size = size
