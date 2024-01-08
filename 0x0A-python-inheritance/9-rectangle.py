#!/usr/bin/python3
"""A class that inherits from BaseGeometry"""
BaseGeomerty = __import__('7-base_geomerty.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Reperesents a rectangle using the inherited class"""

    def __init__(self, width, height):
        """initialization of a new rectangle

        Args:
            width (int) : The width of the rectangle
            height (int) :The height of the rectangle
        """
        super.integer_validator("width", width)
        self.__width = width
        super.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a print() & str() rep of a rec"""
        string = "[" + str(self.__class__.__name__) + "] "
        string = += str(self.__width) + "/" + str(self.__height)
        return string
