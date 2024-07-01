#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    X = len(boxes)
    OPE_NED = [False] * X
    OPE_NED[0] = True
    KEYS = [0]

    while KEYS:
        KEY = KEYS.pop()
        for NEW_KEY in boxes[KEY]:
            if 0 <= NEW_KEY < X and not OPE_NED[NEW_KEY]:
                OPE_NED[NEW_KEY] = True
                KEYS.append(NEW_KEY)

    return all(OPE_NED)
