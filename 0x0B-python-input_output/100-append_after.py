#!/usr/bin/python3
"""
This file contains a function
that inserts a line of text to a file
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function to insert text after a soecific line
    """
    string = ""
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            string += line
            if search_string in line:
                string += new_string

    with open(filename, mode="w") as myFile:
        myFile.write(string)
