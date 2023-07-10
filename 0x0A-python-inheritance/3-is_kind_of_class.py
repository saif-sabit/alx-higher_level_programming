#!/usr/bin/python3
"""Checks object if it is
instance or inherted instance of class"""
def is_kind_of_class(obj, a_class):
    """
    checks if object is
    instance or inherted instance of class
    Args:
    obj(any): object to be checked
    a_class(type): class equals to type of obj
    Returns:
    True: if obj matches the type
    False: otherwise
    """
    if (type(obj) == a_class):
        return (True)
    return False