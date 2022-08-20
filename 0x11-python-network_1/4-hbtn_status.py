#!/usr/bin/python3
'# Write a Python script that fetches '
import requests
<<<<<<< HEAD

x = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}".format(
    type(x.text), x.text))
=======
x = requests.get('https://intranet.hbtn.io/status')
print("Body response:\n\t- type: {}\n\t- content: {}".format(type(x.text), x.text))
>>>>>>> 9f795d13e3cefa43b6577a03b298643228915f7e
