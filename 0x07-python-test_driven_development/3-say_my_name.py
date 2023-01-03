#!/usr/bin/python3

"""
SayMyName module
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'
    Args:
        first_name (str): the first name
        last_name (str): the last name
    Raises:
        TypeError: if one of the first_name and the last_name isn't a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
