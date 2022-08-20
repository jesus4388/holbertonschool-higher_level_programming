#!/usr/bin/python3
'# script that takes 2 arguments in order to solve this challenge'
import requests
from sys import argv

if __name__ == "__main__":
    rname = argv[1]
    ownern = argv[2]

    response = requests.get(
            'https://api.github.com/repos/{}/{}/commits'.format(
                ownern, rname)).json()
    for i in range(0, 10):
        if response[i]:
            print("{}: {}".format(
                response[i].get('sha'), response[i].get(
                    'commit').get('author').get('name')))
