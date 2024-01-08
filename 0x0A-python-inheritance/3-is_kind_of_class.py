#!/usr/bin/python3
"""used to check if an object is an instance of an inherited class"""


def is_kind_of_class(obj, a_class):
    """returns true if it is an instance o the class inherired else false"""
    return isinstance(obj, a_class)
