#!/usr/bin/python3
' # a class Rectangle that defines a rectangle'


class Rectangle:

    '#initializacion'
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    '#Public instance method: def area(self):\
            that returns the rectangle area'
    def area(self):
        return self.__width * self.__height

    '# Public instance method: def perimeter(self):\
            that returns the rectangle perimeter'
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    '# property to retrieve it'
    @property
    def width(self):
        return self.__width

    '# property to retrieve it'
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    '# property to retrieve it'
    @property
    def height(self):
        return self.__height

    '#property setter to set it'
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
