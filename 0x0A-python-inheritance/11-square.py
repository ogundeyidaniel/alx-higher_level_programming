#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    Attributes:
        size (int): the size of the square
    """
    def __init__(self, size):
        """Initializer"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the Square area"""
        return self.__size**2

    def __str__(self):
        """Humain reading representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
