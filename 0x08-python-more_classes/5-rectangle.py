#!/usr/bin/python3
"""
Rectangle Module - Create a rectangle class
"""


class Rectangle:
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """return string representation of rectangle"""
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            rect += '#' * self.width
            if i < self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """return string representation of rectangle to recreate a new instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
