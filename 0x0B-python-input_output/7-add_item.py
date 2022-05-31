#!/usr/bin/python3
'# a script that adds all arguments to a Python lisi'


from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    item = load_from_json_file("add_item.json")
except Exception:
    item = []

item += argv[1:]
save_to_json_file(item, "add_item.json")
