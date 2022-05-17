#!/usr/bin/python3
'# a class Square that defines a square'


class Square:
    '# Private instance attribute: size'
    def __init__(self, size=0):
        '# size and type verification'
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    '# Método de instancia pública'
    def area(self):
        return self.__size * self.__size

    '# property def size(self): to retrieve it'
    @property
    def size(self):
        return self.__size

    '# property setter def size(self, value): to set it'
    @size.setter
    def size(self, val):
        if type(val) is not int:
            raise TypeError('size must be an integer')
        if val < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = val
