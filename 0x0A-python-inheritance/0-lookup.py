#!/usr/bin/python3
"""Defines an object attribute for the lookup function"""


def lookup(obj):
    """Returns a ist of available attributes of an object"""
    return dir(obj)
