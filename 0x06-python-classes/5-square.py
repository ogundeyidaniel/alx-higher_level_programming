#!/usr/bin/python3
class Square():
    """A square class."""

    def __init__(self, size=0):
        """Initialize class."""
        self.size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve size of Square class."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of Square class."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
