#!/usr/bin/python3
'# class Rectangle that inherits from BaseGeometryi'


BaseGeometry = __import__('7-base_geometry').BaseGeometry
'# import '


class Rectangle(BaseGeometry):
    '# class Rectangle that inherits from BaseGeometryi'

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    '# validator of area'
    def area(self):
        return self.__width * self.__height

    'concat widch and height'
    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
