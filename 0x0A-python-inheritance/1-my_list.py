#!/usr/bin/python3
"""mylist inherits list from nother class"""


class MyList(list):
    """used to come up with a sorted list using an inherited class list"""

        def print_sorted(self):
            """print the list in ascending order"""
            sorted_list = sorted(self)
            print(sorted_list)
