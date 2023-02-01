#!/usr/bin/python3
""" class Student to define a student
by: (based on 10-student.py) """


class Student:
    """ Student class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert Student object to JSON"""
        if attrs is None:
            return vars(self)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = vars(self)[i]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """ replace attributes """
        self.__dict__.update(json)
