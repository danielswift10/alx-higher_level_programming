#!/usr/bin/python3
"""
a square module
"""


class Square:
    """
    Definition of a Class Square
    """
    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        set square area
        Return:
            the current square area (int)
        """
        return self.__size * self.__size
