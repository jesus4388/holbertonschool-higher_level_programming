#!/usr/bin/python3
'# a class Rectangle that defines a rectangle'


class Rectangle:

    '# Private instance attribute: width and height'
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if height < 0:
            raise ValueError('width must be >= 0')
        self.__height = height
        self.__width = width

    '# property to get it back'
    @property
    def height(self):
        return self.__height

    '# property setter to set it'
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    '# property to get it back'
    @property
    def width(self):
        return self.__width

    '# property setter to set it'
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
