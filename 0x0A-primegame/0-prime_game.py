#!/usr/bin/python3
"""Module for Prime game."""


def S(M):
    """Generates a list where the index represents the number,
       and the value at each index indicates whether it is prime."""
    P = [True] * (M + 1)
    P[0] = P[1] = False  # 0 and 1 are not primes
    P = 2
    while P * P <= M:
        if P[P]:
            for i in range(P * P, M + 1, P):
                P[i] = False
        P += 1
    return P


def C(P, N):
    """For each N, count how many primes are available.
       The winner of the round depends on the parity of
       this count (odd or even)."""
    R = 0
    for i in range(2, N + 1):
        if P[i]:
            R += 1
    return R % 2


def isWinner(x, nums):
    """Determine the Round Winner."""
    if x <= 0 or not nums:
        return None

    M = max(nums)
    P = S(M)

    M_Wins = 0
    B_Wins = 0

    for N in nums:
        if N == 1:
            B_Wins += 1
        else:
            if C(P, N) == 1:
                M_Wins += 1
            else:
                B_Wins += 1

    if M_Wins > B_Wins:
        return "Maria"
    elif B_Wins > M_Wins:
        return "Ben"
    else:
        return None
