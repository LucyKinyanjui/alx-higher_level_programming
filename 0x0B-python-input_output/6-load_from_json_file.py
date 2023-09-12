#!/usr/bin/python3
"""
file with function that creates an object from json file
"""


import json


def load_from_json_file(filename):
    """
    function to create object from json file
    """
    with open(filename) as myFile:
        new_obj = json.load(myFile)
    return (new_obj)
