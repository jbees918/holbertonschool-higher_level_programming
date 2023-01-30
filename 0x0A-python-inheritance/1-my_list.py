#!/usr/bin/python3
"""Inheritance second task"""


class MyList(list):
    """list and then some"""
    def print_sorted(self):
        _t = self[:]
        _t.sort()
        print(_t)
