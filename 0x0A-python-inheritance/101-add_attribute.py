def add_attribute(obj, attr, value):
    """Add attribute `attr` with value `value` to `obj` if possible.

    Args:
        obj: The object to add an attribute to.
        attr: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If `obj` does not support adding new attributes.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
