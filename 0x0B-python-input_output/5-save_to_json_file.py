#!/usr/bin/python3
'# a function that writes an Object to a text file,\
        using a JSON representation'


import json


def save_to_json_file(my_obj, filename):
    '# object to a text file'

    dict_json = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(dict_json)
