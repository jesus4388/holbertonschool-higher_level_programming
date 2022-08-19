#!/bin/bash
#ash script that takes in a URL and displays all HTTP methods
curl -sI -X -OPTIONS "$1" | grep -i Allow: | cut -d' ' -f2-
