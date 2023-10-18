#!/usr/bin/python3
"""
This module creates a class
student with defined attributes
"""


class Student:
    """class defining attrributes
    """
    def __init__(self, first_name, last_name, age):
        """
        instantiation of attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns dictionary rep of all instances
        """
        if attrs is None:
            return (self.__dict__)
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

    def reload_from_json(self, json):
        """"
        function that replaces all attributes of
        the student instance
        """
        self.__dict__.update(json)
