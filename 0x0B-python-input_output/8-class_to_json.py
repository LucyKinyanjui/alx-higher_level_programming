#!/usr/bin/python3
"""
file has function that returns the dictionary description
with simple data structure for json serialization of object
"""


def class_to_json(obj):
    """
    function that returns dict description
    """
    return (obj.__dict__)
