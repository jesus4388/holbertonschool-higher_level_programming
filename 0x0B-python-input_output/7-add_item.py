#!/usr/bin/python3

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

item = load_from_json_file("add_item.json")
save_to_json_file(item + argv[1], "add_item.json")
