#!/usr/bin/python3
'# Write a class Rectangle that defines a rectangle'


class Rectangle:
    '# Instantiation'
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    '# Public instance method: def area(self):\
    that returns the rectangle area'
    def area(self):
        return self.__width * self.__height

    '# Public instance method: def perimeter(self):\
            that returns the rectangle perimeter'
    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    '# property def width(self): to retrieve it'
    @property
    def width(self):
        return self.__width

    '# property setter def width(self, value): to set it:'
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.width = value

    '# property def height(self): to retrieve it'
    @property
    def height(self):
        return self.__height

    '# property setter def height(self, value): to set it'
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif valur < 0:
            raise ValueError('width must be >= 0')
        else:
            self.height = value

    '# return a string representation of the rectangle'
    def __str__(self):
        cadena = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    cadena += "#"
                cadena += "\n"
            cadena = cadena.rstrip('\n')
            return cadena

    '# print the rectangle with the character #'
    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'
