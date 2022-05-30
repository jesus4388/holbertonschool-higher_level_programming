#!/usr/bin/python3
'# a class Square that inherits from Rectangle'


Rectangle = __import__('9-rectangle').Rectangle
'import module'


class Square(Rectangle):
    '# instance'

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def __str__(self):
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
