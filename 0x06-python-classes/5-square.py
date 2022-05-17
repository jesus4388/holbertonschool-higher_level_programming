#!/usr/bin/python3
'# a class Square that defines a square'


class Square:
    '#Private instance attribute: size:'
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    '# Public instance method'
    def area(self):
        return self.__size * self.__size

    '# propiedad def size(self): para recuperarlo'
    @property
    def size(self):
        return self.__size

    '# property setter def size(self, value): to set it'
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    """Public instance method, that prints \
            in stdout the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for colum in range(0, self.__size):
                for line in range(0, self.__size):
                    print('#', end="")
                print('\n', end="")
