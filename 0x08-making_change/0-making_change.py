#!/usr/bin/python3
"""This script determines the minimum number of coins needed"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    """

    if total <= 0:
        return 0

    CC = 0
    R = total
    IDX = 0
    S_L_C = sorted(coins, reverse=True)
    N = len(coins)

    while R > 0:
        if IDX >= N:
            return -1
        if R - S_L_C[IDX] >= 0:
            R -= S_L_C[IDX]
            CC += 1
        else:
            IDX += 1

    return CC
