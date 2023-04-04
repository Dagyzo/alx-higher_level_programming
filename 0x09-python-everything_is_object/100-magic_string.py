#!/usr/bin/python3

def magic_string():
    """Returns a string "BestSchool" n times the number of the iteration."""
    magic = "BestSchool"
    n = magic_string.counter
    magic_string.counter += 1
    return ", ".join([magic] * n)

magic_string.counter = 1
