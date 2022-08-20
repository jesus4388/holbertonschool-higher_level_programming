#!/usr/bin/python3
'# Python script that takes in a URL'
import requests
from sys import argv

if __name__ == "__main__":

    x = requests.get(argv[1])
    if x.status_code < 400:
	print(x.text)
    else:
	print("Error code: {:}".format(x.status_code))
