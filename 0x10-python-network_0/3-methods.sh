#!/bin/bash
#ash script that takes in a URL and displays all HTTP methods
curl -sI -X -OPTIONS ubuntu@3.80.74.192 | grep -i Allow: | cut -d' ' -f2-
