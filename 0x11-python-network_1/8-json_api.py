#!/usr/bin/python3
'# Python script that takes in a letter and sends a POST'
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        ap = {'q': argv[1]}
    else:
        ap = {'q': ""}
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', ap).json()
        if len(r) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r['id'], r['name']))
    except Exception:
        print("Not a valid JSON")
