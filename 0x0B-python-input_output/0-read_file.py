#!/usr/bin/python3
"""
This file contains a function to print
text file to stdout without implementing import
"""


def read_file(filename=""):
    """
    Function to read the text file and print t stdout
    """
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
