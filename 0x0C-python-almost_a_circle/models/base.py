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

    def to_json_string(list_dictionaries):
        if len(list_dictionaries) == 0 or list_dictionaries == None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []
        if list_objs == None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write([])
        else:
            for i in list_objs:
                lists.append(cls.to_dictionary(i))
            with open(cls.__name__ + ".json", "w") as f:
                    f.write(cls.to_json_string(lists))

    @staticmethod
    def from_json_string(json_string):
        if json_string == None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dum = cls(1, 2)
        dum.update(**dictionary)
        return(dum)
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        new = {}
        lists = []
        if cls == None:
            return new
        else:
            with open(filename, "r") as f:
                new = json.load(f)
            for i in new:
                lists.append(cls.create(**i))
            return lists

