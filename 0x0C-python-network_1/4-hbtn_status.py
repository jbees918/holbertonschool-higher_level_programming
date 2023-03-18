#!/usr/bin/python3
"""
Write a Python script to fetch
https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))
