#!/usr/bin/python3
"""
File contains function that returns
JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Function to return JSON representation
    Args:
        my_obj: object
    """
    return (json.dumps(my_obj))
