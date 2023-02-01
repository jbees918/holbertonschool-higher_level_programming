#!/usr/bin/python3
""" writes a string to text file (UTF8)
returns number of characters written """


def write_file(filename="", text=""):
    """ Reads and prints to stdout """
    with open(filename, "w", encoding="utf-8") as my_file:
        return(my_file.write(text))
