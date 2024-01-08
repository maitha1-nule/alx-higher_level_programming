#!/usr/bin/python3
"""mylist inherits list from nother class"""


class MyList(List):
    """Implements an inherited class called List"""

    def print_sorted(self):
        """prints the list in a sorted manner"""
        sorted_list = sorted(self)
        print(sorted_list)
