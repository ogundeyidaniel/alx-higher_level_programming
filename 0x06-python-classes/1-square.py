#!/usr/bin/python3
"""Square module"""


class Square:
    """
    Square define a geometric shape square
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size):
        """
        Init method is a constructor fo Square class
        Args:
            size (int): the size of the square
        """
        self.__size = size
