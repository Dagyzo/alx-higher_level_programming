#!/usr/bin/python3
class MyInt(int):
    """A rebel int class"""

    def __eq__(self, other):
        """Invert == operator"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Invert != operator"""
        return int(self) == int(other)
