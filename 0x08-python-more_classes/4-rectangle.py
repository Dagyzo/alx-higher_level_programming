#!/usr/bin/python3
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes an instance of the Rectangle class"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the Rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Returns a string representation of the Rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect_str = ""
            for i in range(self.height):
                rect_str += "#" * self.width
                if i != self.height - 1:
                    rect_str += "\n"
            return rect_str

    def __repr__(self):
        """Returns a string representation of the Rectangle that can be used to recreate it"""

        return "Rectangle({}, {})".format(self.width, self.height)
