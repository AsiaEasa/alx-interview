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
    for i in range(COL):
        if BOARD[ROW][i] == 1:
            return False

    for i, j in zip(range(ROW, -1, -1), range(COL, -1, -1)):
        if BOARD[i][j] == 1:
            return False

    for i, j in zip(range(ROW, len(BOARD), 1), range(COL, -1, -1)):
        if BOARD[i][j] == 1:
            return False

    return True


def SOLVE_N_QUEENS(BOARD, COL):
    if COL >= len(BOARD):
        PRINT_SOLUTION(BOARD)
        return True

    res = False
    for i in range(len(BOARD)):
        if IS_SAFE(BOARD, i, COL):
            BOARD[i][COL] = 1
            res = SOLVE_N_QUEENS(BOARD, COL + 1) or res
            BOARD[i][COL] = 0

    return res


def PRINT_SOLUTION(BOARD):
    solution = []
    for i in range(len(BOARD)):
        for j in range(len(BOARD)):
            if BOARD[i][j] == 1:
                solution.append([i, j])
    print(solution)


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
