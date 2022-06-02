#!/usr/bin/python3
'# class Student that defines a student by:\
        (based on 9-student.py)'


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dict1 = {}
        if type(attrs) is not list:
            return self.__dict__
        if all(isinstance(_str, str)for _str in attrs):
            for key, value in self.__dict__.items():
                if key in attrs:
                    dict1[key] = value
            return dict1
        else:
            return self.__dict__
