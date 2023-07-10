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
    self.integer_validator("width",width)
    self.__width = width
    self.integer_validator("height",height)
    self.__height = height