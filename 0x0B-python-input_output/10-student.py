#!/usr/bin/python3
'# class Student that defines a student by:\
        (based on 9-student.py)'


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return self.__dict__
        for x in attrs:
            if type(attrs) is str:
                return self.__dict__
        else:
            _dict = {}
            for key, value in self.__dict__.items():
                for x in attrs:
                    if x == key:
                        _dict.update({key: value})
            return _dict
