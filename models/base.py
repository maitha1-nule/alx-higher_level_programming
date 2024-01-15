#!/usr/bin/python3
"""
This is the main module of this poject
"""


class Base():
    """This is the main class for this object.
    
    Args:
        __nb_object : this is a private attribute.
        id: is also assigned 0.
        """
        __nb_objects = 0

        def __init__(self, id=None):
            if id is not None:
                self.id = id
            else:
                Base.__nb-objects += 1
                self.id = Base.__nb_objects


