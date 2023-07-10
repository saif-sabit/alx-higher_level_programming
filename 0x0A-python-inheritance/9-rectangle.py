#!/usr/bin/python3
""" Defining Rectangle class"""
BaseGeometry =__import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ represents the Rectangle class """
def __init__(self, width, height):
    """ inialize height and width
    Args:
    width(int): width of rectangle
    height(int): height of rectangle"""
    BaseGeometry.integer_validator("width",width)
    self.__width = width
    BaseGeometry.integer_validator("height",height)
    self.__height = height
    def area(self):
        """ returns area of rectangle"""
        return self.__height * self.__width
    def __str__(self):
        """ prints representation of class"""
        return "[Rectangle] {} / {}".format(str(self.__width),str(self.__height))