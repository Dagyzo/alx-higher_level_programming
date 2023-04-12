#!/usr/bin/python3
"""Defines an inherited list class My List."""


class My List(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))
