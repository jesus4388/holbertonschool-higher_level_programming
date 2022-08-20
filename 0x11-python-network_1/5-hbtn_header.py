#!/usr/bin/python3
'# a Python script that takes in a URL'
import requests
from sys import argv

if __name__ == "__main__":
    x = requests.get(argv[1])
    print(x.headers.get("X-Request-Id"))
