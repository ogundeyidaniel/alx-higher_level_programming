#!/usr/bin/python3
"""Is inheerit from module"""


def inherits_from(obj, a_class):
    """Returns if the object is an instance of a the given class
    that inherited (directly/indirectly) from the specified class
    Args:
        obj (object): the given object
        a_class (class): the given class
    Return:
        (True) if a sublclass
        (False) otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
