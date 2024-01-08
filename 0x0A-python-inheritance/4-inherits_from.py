#!/usr/bin/python3
"""Checks whether an object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """returns true if a class is a sub class of another class"""
    return issubclass(obj, a_class)
