#!/usr/bin/python3
"""Rebelion integer module"""


class MyInt(int):
    """Myint class"""
    def __eq__(self, other):
        """Equity comparaison"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Not equity comparaison"""
        return not super().__ne__(other)
