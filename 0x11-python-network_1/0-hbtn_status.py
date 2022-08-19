#!/usr/bin/python3
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:\n    -type: {}\n    -content: {}".format(
    type(html), html))
print("    -utf8 content: {}".format(html.decode()))
