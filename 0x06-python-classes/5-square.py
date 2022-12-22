#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    Square define a geometric shape square
    Attributes:
        __size (int): the size of the square
    """
    def __init__(self, size=0):
        """
        Init method is a constructor fo Square class
        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter of instance attributes
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of instance attributes
        Args:
            value (int): an integer assigned to to the square size
        Raises:
            TypeError: if size not an integer
            ValueError: if size less than 0
        """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Area returns the current square area
        Returns:
            integer: the square area
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square forming by '#' symbol
        """
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                print('#'*self.__size)
