#!/usr/bin/python3
"""
File with function that appends a string at the end
of a text file and returns the # of characters added
"""


def append_write(filename="", text=""):
    """
    fucntion that appends a string at the end of a text file
    and returns number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
