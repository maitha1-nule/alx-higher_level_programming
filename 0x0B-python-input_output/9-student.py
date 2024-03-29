#!/usr/bin/python3
"""A script that defines a student class"""


class Student():
    """represents a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialization of a new student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
