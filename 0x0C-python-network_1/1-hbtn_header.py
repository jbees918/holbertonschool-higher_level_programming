#!/usr/bin/python3
"""
 Python script to take in a URL,
 sends a request to the URL and displays
 the value of the X-Request-Id variable found
 in the header of the response.
"""
from urllib import request
import sys


if __name__ == "__main__":
    html = request.Request(sys.argv[1])
    with request.urlopen(html) as response:
        print(response.info()['X-Request-Id'])
