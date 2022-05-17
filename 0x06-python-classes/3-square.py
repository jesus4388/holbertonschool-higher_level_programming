#!/usr/bin/python3
'# a class Square that defines a square'


class Square:
    '# Private instance attribute: size'
    def __init__(self, size=0):
        '# size and type verification'
        if not(type(size) == int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    """Public instance method: def area(self): \
            that returns the current square area"""
    def area(self):
        return self._Square__size * self._Square__size
