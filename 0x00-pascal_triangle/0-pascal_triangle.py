#!/usr/bin/python3
"""A module to build a triangle"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []

    TRI = [[1]]

    for i in range(1, n):
        ROW = [1]
        for j in range(1, i):
            ROW.append(TRI[i-1][j-1] + TRI[i-1][j])
        ROW.append(1)
        TRI.append(ROW)

    return TRI
