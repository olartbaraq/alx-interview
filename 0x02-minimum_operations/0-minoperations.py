#!/usr/bin/python3

"""
This code requires two operations(copy all and paste) to determine
the minimum operations to be carried to result to the number of
characters to be determined
"""


def minOperations(n: int) -> int:
    """
    returns the minimum number of operations
    required to get the character argument
    """
    if (n < 2):
        return 0

    single_character = 1
    character_count = 0
    character_buffer = 0

    while (single_character < n):
        remaining_character = n - single_character

        if (remaining_character % single_character == 0):
            character_buffer = single_character
            single_character += character_buffer
            character_count += 2

        single_character += character_buffer
        character_count += 1

    return character_count
