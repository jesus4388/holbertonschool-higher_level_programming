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

        self.id = id
        
        if self.id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        if list_dictionaries == None or len(list_dictionaries) == 0:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        lists = []
        if list_objs == None:
            return lists
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
        new = cls(1, 2)
        new.update(**dictionary)
        return(new)
