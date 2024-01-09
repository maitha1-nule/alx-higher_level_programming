#!/usr/bin/python3
"""A script that returns an object rep by json"""
import json


def from_json_string(my_str):
    """The function that converts the object.
    Args:
        my_str (str): the file to be retuned
    """
    return json.loads(my_str)
