#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
