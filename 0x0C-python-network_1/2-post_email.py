#!/usr/bin/python3
"""
Python script to take
in a URL and an email, sends
a POST request to the passed URL
with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
