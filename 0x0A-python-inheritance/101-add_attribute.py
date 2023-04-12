def add_attribute(obj, attr, value):
    """Add attribute `attr` with value `value` to `obj` if possible.

    Args:
        obj: The object to add an attribute to.
        attr: The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If `obj` does not support adding new attributes.
    """
    if not hasattr(obj, '__dict__') and not (hasattr(type(obj), '__slots__') and attr in type(obj).__slots__):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
