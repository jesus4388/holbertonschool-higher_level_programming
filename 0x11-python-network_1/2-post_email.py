#!/usr/bin/python3
'# python script that takes in a URL and an email'
from sys import argv
import urllib.request

if __name__ == "__main__":

    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode()

    with urllib.request.urlopen(url, data) as resp:
        response = resp.read()
        print(response.decode())
