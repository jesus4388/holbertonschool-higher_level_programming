#!/usr/bin/python3
'# Write a class Student that defines a student by'


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return self.__dict__
        for x in attrs:
            if type(x) is str:
                return self.__dict__
        else:
            _dict = {}
            for key, value in self.__dict__.item():
                for x in attrs:
                    if key == x:
                        _dict.update({key: value})

    def reload_from_json(self, json):
        for key, value in json.item():
            for i, j in self.__dict__.item():
                if key == i:
                    self.__dict.update({key: value})
