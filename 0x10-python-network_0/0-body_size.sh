#!/bin/bash
#Bash script that takes in a URL, sends a request to that URL
echo -sI "$1" | grep -i "Content-Lenth" | "{ print $2 }"
