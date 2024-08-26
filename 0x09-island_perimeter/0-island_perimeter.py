#!/usr/bin/python3
""" This module contains the solution for the Island"""


def island_perimeter(grid):
    """Calculates and returns the perimeter"""

    P = 0
    R = len(grid)
    C = len(grid[0])

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    P += 1
                if r == R-1 or grid[r+1][c] == 0:
                    P += 1
                if c == 0 or grid[r][c-1] == 0:
                    P += 1
                if c == C-1 or grid[r][c+1] == 0:
                    P += 1

    return P
