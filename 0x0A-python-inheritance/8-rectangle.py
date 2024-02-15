#!/usr/bin/python3
"""Thi will be a rectangle class which inherits from basegeomety"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this is the child class of the parent class BaseGeometry"""

    def __init__(self, width, height):
        """initialializing of a new rectangle.

        Args:
            width (int) : the width of the new rectngle.
            height (int) : The height of the new rectangle.
            """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
