#!/usr/bin/python3
"""A script that returns the JSON repreentation of a string"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
