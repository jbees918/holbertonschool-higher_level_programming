#!/usr/bin/python3
""" returns JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """Converts object to JSON."""
    return json.dumps(my_obj)
