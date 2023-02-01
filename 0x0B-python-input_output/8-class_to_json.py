#!/usr/bin/python3
""" returns dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object: """


def class_to_json(obj):
    """ returns dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object: """

    return vars(obj)
