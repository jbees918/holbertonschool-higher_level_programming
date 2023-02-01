#!/usr/bin/python3
"""
Auther: Josh Beeson
Date: Jan, 2023
class MyList that inherits from list
"""


class MyList(list):
    """ Inherits from list """

    def print_sorted(self):
        """ Prints sorted list (ascending) """

        print(sorted(self))
