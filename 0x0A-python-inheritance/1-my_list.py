#!/usr/bin/python3
"""
Module MyList class
"""


class MyList(list):
    """Type class MyList that inherits from list"""

    def print_sorted(self):
        """
        Public instance method that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
