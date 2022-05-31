#!/usr/bin/python3
'# a function that creates an Object from a “JSON file”'


import json


def load_from_json_file(filename):
    '# creat an onject'

    with open(filename, 'r') as f:
        _read = f.read()
    return json.loads(_read)
