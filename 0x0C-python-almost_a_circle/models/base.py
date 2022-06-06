#!/usr/bin/python3
'# Write the first class Base'


import json
'i# import json'


class Base:
    '# first class base'

    __nb_objects = 0
    '# private class atribute'

    def __init__(self, id=None):
        '# method constructor'

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '# return representation string of json'
        if list_dictionaries is None:
            list_dictionaries = "[]"
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '# save to file'
        lists = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(lists))
        else:
            for i in list_objs:
                lists.append(cls.to_dictionary(i))
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        '# from json string'
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '# dummy instance'
        dum = cls(1, 2)
        dum.update(**dictionary)
        return(dum)

    @classmethod
    def load_from_file(cls):
        '# load file'
        filename = cls.__name__ + ".json"
        new = {}
        lists = []
        if cls is None:
            return new
        else:
            with open(filename, "r") as f:
                new = json.load(f)
            for i in new:
                lists.append(cls.create(**i))
            return lists
