#!/usr/bin/python3
'# class Rectangle that inherits from BaseGeometry'


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'# import module'


class Rectangle(BaseGeometry):
    '# class Rectangle that inherits from BaseGeometry'

    def __init__(self, width, height):
        '# validator of integer'

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
