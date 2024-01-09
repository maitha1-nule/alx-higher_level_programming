#!/usr/bin/python3
"""A scrpit which appends to a file"""


def append_write(filename="", text=""):
    """The function to append.

    Args:
        filename (str): The file to Append.
        text (str): The file to be returned.

    Returns:
        The appendes function.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
