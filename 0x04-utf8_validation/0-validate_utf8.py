#!/usr/bin/python3
"""Determines a valid UTF-8 encoding"""


def validUTF8(data):
    """
    Checks if a list of integers (data) is valid UTF-8 encoding
    """
    NUM_BYTES = 0

    MASK1 = 1 << 7
    MASK2 = 1 << 6

    if not data or len(data) == 0:
        return True

    for NUM in data:
        BYTE = NUM & 0xFF
        
        if NUM_BYTES == 0:
            MASK = 1 << 7
            while MASK & BYTE:
                NUM_BYTES += 1
                MASK = MASK >> 1
            
            if NUM_BYTES == 0:
                continue
            
            if NUM_BYTES == 1 or NUM_BYTES > 4:
                return False
        else:
            if not (BYTE & MASK1 and not (BYTE & MASK2)):
                return False
        
        NUM_BYTES -= 1
    return NUM_BYTES == 0
