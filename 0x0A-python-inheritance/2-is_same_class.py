#!/usr/bin/python3
""" define object checking"""
def is_same_class(obj, a_class):
    """ checks is object is 
    instance of a given class
    Args:
    obj(any): object for checking
    a_class(type): class to check if parent
    Returns:
    True: if object is instance of the class
    False: otherwise"""
    if (type(obj) ==a_class ):
        return (True)
    return (False)