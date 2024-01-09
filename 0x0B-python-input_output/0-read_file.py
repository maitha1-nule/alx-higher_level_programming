#!/usr/bin/python3
"""A function that reads a file and prints it"""


def read_file(filename=""):
    """This is the function to use

    Args:
        filename which is not initialized
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading the file: {e}")
