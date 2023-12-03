#!/usr/bin/python3
"""
-takes a URL and email
-sends a POST request to the passed url
-

"""
import sys
import urllib.request
if __name__ == "__main__":

    email = sys.argv[2]
    url = sys.argv[1]

    with urllib.request.urlopen(url, data=email.encode('utf-8')) as response:
        print(response.reade().decode('utf-8'))
