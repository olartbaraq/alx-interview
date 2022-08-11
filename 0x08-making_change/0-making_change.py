#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given smount

    Args:
        coins (List): a list of coins available
        total (sum): the total sum needed to complete target
    """

    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1
