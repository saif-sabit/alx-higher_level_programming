#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Rectangle class body."""

    def __init__(self, width=0, height=0):
        """Initialize

        Args:
            width (int): The width
            height (int): The height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get - set height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        