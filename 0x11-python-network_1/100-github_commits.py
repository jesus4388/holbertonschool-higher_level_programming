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
    if len(response) > 0:
        iterador = 10
    else:
        iterador = len(response)
    try:
        for it in range(iterador):
            print("{}: {}".format(
                response[it].get('sha'), response[it].get(
                    'commit').get('author').get('name')))
    except Exception:
        pass
