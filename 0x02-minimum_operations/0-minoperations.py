#!/usr/bin/python3
"""Module to calculate the minimum number of operations"""


def minOperations(i):
    """Calculate the fewest number of operations"""
    if i <= 1:
        return 0
    Op = 0
    Fa = 2
    while i > 1:
        while i % Fa == 0:
            Op += Fa
            i //= Fa
        Fa += 1
    return Op
