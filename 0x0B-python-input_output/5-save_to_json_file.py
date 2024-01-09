#!/usr/bin/python3
"""A script that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """This is the function that writes an object to a textfile.

    Args:
        my_obj (str): this is the function to be written.
        filename (str): the file to be written.
    """
    with open(my_obj, "w") as file:
        return json.dump(my_obj, file)
