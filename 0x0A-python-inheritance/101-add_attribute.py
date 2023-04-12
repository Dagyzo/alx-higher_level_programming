#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Agrs:
        obj (any): The oject to add attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of the att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "_dict_"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)