#!/usr/bin/python3
"""
File with function that writes an object
to a txt file using json representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function to write an object to text file using json
    """
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
