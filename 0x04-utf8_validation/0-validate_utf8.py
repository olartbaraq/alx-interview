#!/usr/bin/python3
"""
main file for the utf-8 code
"""


def validUTF8(data):
    """
    function to return if an array of
    integer is a valid UTF8 caharacter
    """
    def length(n):
        """returns the length of the binary code
        converted from integer
        """
        return len('{:08b}'.format(n).split('0', 1)[0])

    i = 0
    while i < len(data):
        le = length(data[i])
        i += 1
        if le == 1 or le > 4:
            return False
        if le > 1:
            for _ in range(le - 1):
                if i == len(data) or length(data[i]) != 1:
                    return False
                i += 1
    return True
