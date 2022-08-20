#!/usr/bin/python3
'# Write a Python script that fetches '
import requests

x = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}".format(
    type(x.text), x.text))
