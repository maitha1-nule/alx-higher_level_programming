#!/usr/bin/python3
"""continuation of the basegeometry task from tast 5"""


class BaseGeometry():
    """This is the parent class that were going to be using"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise Exception(f"{name} must be an integer")
        elif value <= 0:
            raise Exception(f"{name} must be greater than 0")
