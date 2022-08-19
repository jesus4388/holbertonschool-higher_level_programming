#!/bin/bash
#Bash script that takes in a URL as an argument
curl -s -X POST --data "email=test@gmail.com" --data "subject=I will always be here for PLD" "$1"
