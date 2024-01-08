#!/usr/bin/python3
"""continuation of the basegeometry task from tast 5"""


class BaseGeometry():
    """This is the parent class that were going to be using"""

    def area(self):
        """implemention later"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the integers entered
        Args:
        name (str): The name of the parameter.)
        value (int): The parameter to validate.
        Raises:
        TypeError: If value is not an integer
        ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
