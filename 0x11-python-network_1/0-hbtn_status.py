#!/usr/bin/python3
"""makes a get request to 'https://alx-intranet.hbtn.io/status'
"""
from urllib.request import urlopen
url = "https://alx-intranet.hbtn.io/status"
with urlopen(url) as response:
    body = response.read()
print('Body response:')
print("\t- type: {}".format(type(body)))
print("\t- content: {}".format(body))
print("\t- utf8 content: {}".format(body.decode('utf8')))
