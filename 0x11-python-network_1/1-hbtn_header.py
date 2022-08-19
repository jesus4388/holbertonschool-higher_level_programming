#!/usr/bin/python3
# a Python script that takes in a URL
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get("X-Request-Id"))
