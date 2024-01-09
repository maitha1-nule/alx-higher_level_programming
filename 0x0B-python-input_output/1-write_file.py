#!/usr/bin/python3
"""A script that writes a striing to a txt file"""


def write_file(filename="", text=""):
    """Writes into a file and return the number of chars

    Args:
        filename (str): this is the file to be written
        text (str): this is the file to be returned to

    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return f.write(text)
