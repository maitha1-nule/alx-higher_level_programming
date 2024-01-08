#!/usr/bin/python3
"""mylist inherits list from nother class"""


class MyList(list):
    def __init__(self, items):
        self.items = items
        super().__init__(items)

        def print_sorted(self):
            """print the list in ascending order"""
            sorted_list = sorted(self)
            print(sorted_list)
