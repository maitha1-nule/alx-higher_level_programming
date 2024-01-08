#!/usr/bin/python3
"""Used to define an attribute(obj) that belongs to the lookup function"""

def lookup(obj):
"""Returns a ist of available attributes of an object"""
    return dir(obj)
