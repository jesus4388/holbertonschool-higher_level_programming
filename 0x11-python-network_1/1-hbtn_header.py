#!/usr/bin/python3
# a Python script that takes in a URL

import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.read()
    print(response.info().get("X-Request-Id"))
