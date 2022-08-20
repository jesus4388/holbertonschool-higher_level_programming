#!/usr/bin/python3 
'# python script that takes in a URL and an email' 
from sys import argv
import urllib.request
from urllib.error import HTTPError

if __name__ == "__main__":
	try:
		with urllib.request.urlopen(argv[1]) as resp:
			response = resp.read()
			print(response.decode())
	except HTTPError as err:
		print("Error code: {}".format(err.code))
