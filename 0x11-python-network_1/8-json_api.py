#!/usr/bin/python3
'# Python script that takes in a letter and sends a POST'
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        ap = argv[1]
    else:
        ap = ""
    r = requests.post('', data={'ap': ap})
    try:
        jd = r.json()
        if len(jd.keys()) > 0:
            print("[{:}] {:}".format(jd.get('id'), jd.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
