#!/usr/bin/python3
"""Module containing lookup function to get the list of available attributes and methods of an object"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: Object to get attributes and methods of.
    :type obj: object
    :return: List of available attributes and methods of the object.
    :rtype: list
    """
    # Get the list of attributes and methods using the built-in function dir()
    attributes_and_methods = dir(obj)

    # Filter out any private or special attributes and methods
    filtered_attributes_and_methods = [
        item for item in attributes_and_methods if not item.startswith("__")]

    # Return the filtered list of attributes and methods
    return filtered_attributes_and_methods
