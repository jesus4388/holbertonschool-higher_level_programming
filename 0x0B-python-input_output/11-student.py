#!/usr/bin/python3
'# Write a class Student that defines a student by'


class Student:

    def __init__(self, first_name, last_name, age):
        '# attributes'

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '# retrieves a dictionary'

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

    def reload_from_json(self, json):
        '#replaces all atributes'

        for key, value in self.__dict__.items():
            if key in json:
                self.__dict__[key] = json[key]

        return self.__dict__
