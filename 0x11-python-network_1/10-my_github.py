#!/usr/bin/python3
'# script de Python que tome sus credenciales de GitHub'
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get("https://api.github.com/user", auth=(
        argv[1], argv[2])).json()

    try:
        print(response['id'])
    except Exception:
        print(None)
