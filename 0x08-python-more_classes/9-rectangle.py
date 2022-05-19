#!/usr/bin/python3
'# Write a class Rectangle that defines a rectangle'


class Rectangle:
    '# Instantiation'

    number_of_instances = 0

    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            self.__width = value

    '# property def height(self): to retrieve it'
    @property
    def height(self):
        return self.__height

    '# property setter def height(self, value): to set it'
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__height = value

    '# return a string representation of the rectangle'
    def __str__(self):
        cadena = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    cadena = cadena + str(self.print_symbol)
                cadena += "\n"
            cadena = cadena.rstrip('\n')
            return cadena

    '# print the rectangle with the character #'
    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    '#  returns the biggest rectangle based on the area'
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    '# eturns a new Rectangle instance'
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
