#!/usr/bin/python3
""" appends string at end of text file (UTF8)
returns number of characters added """


def append_write(filename="", text=""):
    """ Reads and prints to stdout """
    with open(filename, "a", encoding="utf-8") as my_file:
        return(my_file.write(text))
