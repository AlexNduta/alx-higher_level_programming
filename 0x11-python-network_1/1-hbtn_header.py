#!/usr/bin/python3
"""
takes a URL and displays the value of the X-Requrst-Id found in the header of the response
"""
import urllib.request
import sys
url = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(url) as response:
    leader = response.headers
    print(dict(response.headers).get('X-Request-Id'))
