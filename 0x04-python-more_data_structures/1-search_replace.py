#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = my_list[:]
    for i, a in enumerate(new_list):
        if a == search:
            new_list(i) = replace
    return new_list
