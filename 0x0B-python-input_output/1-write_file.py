#!/usr/bin/python3
"""
File contains function that writes
a string to a text file
"""


def write_file(filename="", text=""):
    """
    Function that writes to files
    """
    with open(filename, mode='w', encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
