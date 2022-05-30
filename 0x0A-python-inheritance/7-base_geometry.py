#!/usr/bin/python3

BaseGeometry = __import__('6-base_geometry').BaseGeometry

class BaseGeometry(BaseGeometry):

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name +" must be an integer")
        if value <= 0:
            raise ValueError(name +" must be greater than 0")
