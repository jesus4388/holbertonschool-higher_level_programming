#!/usr/bin/python3
'# a class Square that defines a square'


class Square:
    '# private instance attribute: size'
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    '# size area'
    def area(self):
        return self.__size * self.__size

    '# to retrieve it'
    @property
    def size(self):
        return self.__size

    '# to set it'
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    '# retrieve position and make it private'
    @property
    def position(self):
        return self.__position

    '# set private position attribute'
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    '# my print atribute'
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            position = self.__position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for i in range(self.size):
                print(" " * position[0] + "#" * self.size)
