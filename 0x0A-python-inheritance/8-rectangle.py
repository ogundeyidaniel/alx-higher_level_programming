#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class

    Attributes:
        width (int): the rectangle width
        height (int): the rectangle height
    """
    def __init__(self, width, height):
        """Initializer

        Args:
            width (int): the retangle width
            height (int): the rectangle height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
