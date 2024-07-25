def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    NUM_BYTES = 0

    # Masks to check the significant bits in each byte
    MASK1 = 1 << 7  # 10000000
    MASK2 = 1 << 6  # 01000000

    # For each integer in the data
    for NUM in data:
        # Get the 8 least significant bits of the integer
        BYTE = NUM & 0xFF
        
        if NUM_BYTES == 0:
            # Determine how many bytes the current UTF-8 character has
            MASK = 1 << 7
            while MASK & BYTE:
                NUM_BYTES += 1
                MASK = MASK >> 1
            
            # If NUM_BYTES is 0, then it is a 1-byte character
            if NUM_BYTES == 0:
                continue
            
            # If NUM_BYTES is more than 4 or less than 2, it is invalid
            if NUM_BYTES == 1 or NUM_BYTES > 4:
                return False
        else:
            # Check if it is a continuation byte
            if not (BYTE & MASK1 and not (BYTE & MASK2)):
                return False
        
        # We processed one byte of the UTF-8 character
        NUM_BYTES -= 1
    
    # If we have processed all bytes, NUM_BYTES should be 0
    return NUM_BYTES == 0
