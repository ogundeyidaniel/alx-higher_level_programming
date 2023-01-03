#!/usr/bin/python3

"""
PrintSquare module
"""


def print_square(size):
    """
    Prints a square with the character '#'
    Args:
        size (int): the size length of the square
    Raises:
        TypeError: if size not an integer
        ValueError: if size less than 0
        TypeError: if size is float and less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is 0:
        print()
    for row in range(size):
        print('#'*size)
