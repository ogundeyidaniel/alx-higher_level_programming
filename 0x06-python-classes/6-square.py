#!/usr/bin/python3
class Square():
    """A square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize class."""
        self.size = size
        self.position = position

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
        for row in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def position(self):
        """Retrieve position of Square class."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of Square class."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
