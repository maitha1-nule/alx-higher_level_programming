#!/usr/bin/python3
"""A script that creates an object from a Json file"""
import json


def load_from_json_file(filename):
    """the prototype to use for creation"""
    with open(filename, "r") as file:
        return json.load(file)
