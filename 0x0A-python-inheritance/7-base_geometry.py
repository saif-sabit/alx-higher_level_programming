#!/usr/bin/python3
""" Defining Empty class"""
class BaseGeometry:
    """ represents the BaseGeometry class """
def area(self):
    """ Exception method for the class
    Raises:
    area not implemented
    """
    raise Exception("area() is not implemented")

def integer_validator(self, name, value):
    """ checks integer
    Args:
    name(str): name
    value(int): value to validate
    Raises:
    TypeError: if value is not an integer
    ValueError: if value is < 0"""
    if(type(value) != int):
        raise TypeError("{} must be an integer".format(name))
    if value <= 0:
        raise ValueError("{} must be greater than 0".format(name))
    