#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    dict_json = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(dict_json)
