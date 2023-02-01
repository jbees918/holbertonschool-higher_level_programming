#!/usr/bin/python3
""" returns an object (Python data structure)
represented by JSON string """

import json


def from_json_string(my_str):
    """
    returns object (Python data structure) represented by JSON string
    """
    return json.loads(my_str)
