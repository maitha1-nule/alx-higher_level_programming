#!/usr/bin/python3
"""A function that reads a file and prints it"""


def read_file(filename=""):
    """This is the function to use

    Args:
        filename (str): The file to be read

    Raises:
        Exception: If an error occurs while reading the file
    """
    try:
        with open(filename, 'r', encoding='UTF8') as file:
            for line in file:
                print(line, end='')
    except Exception as e:
        print(f"Error reading the file: {e}")
