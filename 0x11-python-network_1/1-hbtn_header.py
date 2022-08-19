#!/usr/bin/python3
'# python script that takes in a URL and an email'
from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.info().get(X-Request-Id))
