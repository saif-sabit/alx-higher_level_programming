#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Rectangle class body.
    Attributes:
    number_of_instances (int): no of instances
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize

        Args:
            width (int): The width
            height (int): The height
        """
        type(self).number_of_instances += 1
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

    def area(self):
        """get area """
        return (self.__width * self.__height)

    def perimeter(self):
        """get perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return empty string or print rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            shape = []
            for i in range(self.__height):
                for j in range(self.__width):
                    shape.append(str(self.print_symbol))
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """string representation"""
        shape = "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"
        return (shape)

    def __del__(self):
        """delection message"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return greater area retangle.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return Rectangle with size.

        Args:
            size (int): The width and height new Rectangle.
        """
        return (cls(size, size))
