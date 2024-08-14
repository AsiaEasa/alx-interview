#!/usr/bin/python3
"""
Rotate the given N x N 2D MATRIX 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(MATRIX):
    """
    Rotates a given 2D MATRIX 90 degrees clockwise.
    """
    SIZE = len(MATRIX)
    # Rotate the MATRIX layer by layer
    for LAYER in range(SIZE // 2):
        for ELEMENT in range(LAYER, SIZE - LAYER - 1):
            # Perform the 4-way exchange
            TEMP = MATRIX[LAYER][ELEMENT]
            MATRIX[LAYER][ELEMENT] = MATRIX[SIZE - ELEMENT - 1][LAYER]
            MATRIX[SIZE - ELEMENT - 1][LAYER] = (
                MATRIX[SIZE - LAYER - 1][SIZE - ELEMENT - 1]
            )
            MATRIX[SIZE - LAYER - 1][SIZE - ELEMENT - 1] = (
                MATRIX[ELEMENT][SIZE - LAYER - 1]
            )
            MATRIX[ELEMENT][SIZE - LAYER - 1] = TEMP
