#!/usr/bin/python3
"""Module for Prime Game."""


def generatePrimeFlags(maxValue):
    """Generates a list where the index represents the number,
       and the value at each index indicates whether it is prime."""
    primeFlags = [True] * (maxValue + 1)
    primeFlags[0] = primeFlags[1] = False  # 0 and 1 are not primes
    currentPrime = 2
    while currentPrime * currentPrime <= maxValue:
        if primeFlags[currentPrime]:
            for i in range(currentPrime * currentPrime, maxValue + 1, currentPrime):
                primeFlags[i] = False
        currentPrime += 1
    return primeFlags


def calculatePrimeCount(primeFlags, limit):
    """For each limit, count how many primes are available.
       The winner of the round depends on whether the count
       of primes is odd or even."""
    primeCounter = 0
    for i in range(2, limit + 1):
        if primeFlags[i]:
            primeCounter += 1
    return primeCounter % 2


def isWinner(x, nums):
    """Determine the overall winner of the Prime Game."""
    if x <= 0 or not nums:
        return None

    maxValue = max(nums)
    primeFlags = generatePrimeFlags(maxValue)

    mariaWins = 0
    benWins = 0

    for limit in nums:
        if limit == 1:
            benWins += 1
        else:
            if calculatePrimeCount(primeFlags, limit) == 1:
                mariaWins += 1
            else:
                benWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None
