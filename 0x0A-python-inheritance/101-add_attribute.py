#!/usr/bin/python3
"""Add attributes module"""


def add_attribute(obj, key, value):
    """Adds attributes to the given object
    Args:
        obj (object): the given object
        key (object): the given key
        value (object): the given object
    Raises:
        TypeError: If cannot add a new attribute to the object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
