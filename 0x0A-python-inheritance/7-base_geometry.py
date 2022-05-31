#!/usr/bin/python3
'# Write a class BaseGeometry'


BaseGeometry = __import__('6-base_geometry').BaseGeometry
'# import module'


class BaseGeometry(BaseGeometry):
    '# instance'

    def area(self):
        raise Exception("area() is not implemented")

    '# validator of integer'
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
