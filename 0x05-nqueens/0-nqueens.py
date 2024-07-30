#!/usr/bin/python3
"""N queens"""
import sys


def USAGE_ERROR():
    print("Usage: nqueens N")
    sys.exit(1)

def NUMBER_ERROR():
    print("N must be a number")
    sys.exit(1)

def SIZE_ERROR():
    print("N must be at least 4")
    sys.exit(1)

def IS_SAFE(BOARD, ROW, COL):
    for I in range(COL):
        if BOARD[ROW][I] == 1:
            return False

    for I, J in zip(range(ROW, -1, -1), range(COL, -1, -1)):
        if BOARD[I][J] == 1:
            return False

    for I, J in zip(range(ROW, len(BOARD), 1), range(COL, -1, -1)):
        if BOARD[I][J] == 1:
            return False

    return True

def SOLVE_N_QUEENS(BOARD, COL):
    if COL >= len(BOARD):
        PRINT_SOLUTION(BOARD)
        return True

    RES = False
    for I in range(len(BOARD)):
        if IS_SAFE(BOARD, I, COL):
            BOARD[I][COL] = 1
            RES = SOLVE_N_QUEENS(BOARD, COL + 1) or RES
            BOARD[I][COL] = 0

    return RES

def PRINT_SOLUTION(BOARD):
    SOLUTION = []
    for I in range(len(BOARD)):
        for J in range(len(BOARD)):
            if BOARD[I][J] == 1:
                SOLUTION.append([I, J])
    print(SOLUTION)

def MAIN():
    if len(sys.argv) != 2:
        USAGE_ERROR()

    try:
        N = int(sys.argv[1])
    except ValueError:
        NUMBER_ERROR()

    if N < 4:
        SIZE_ERROR()

    BOARD = [[0 for _ in range(N)] for _ in range(N)]
    if not SOLVE_N_QUEENS(BOARD, 0):
        pass

if __name__ == "__main__":
    MAIN()
