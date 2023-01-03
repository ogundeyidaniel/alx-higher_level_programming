#!/usr/bin/python3

"""
TextIndentaion module
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of those characters:
    '.' '?' ':'
    Args:
        text (str): a given string
    Raises:
        TypeError: if argument passed is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for c in text:
        string += c
        if c in ":.?":
            print(string.lstrip(), end="\n\n")
            string = ""
    print(string.lstrip(), end='')
