#!/usr/bin/python3
"""
takes a URL and displays the value of the X-Requrst-Id found in the header of the response
"""
from urllib.request import urlopen
import sys
url = sys.argv[1]
with urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
