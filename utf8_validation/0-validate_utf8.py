#!/usr/bin/python3
"""
Module that validates if a data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    Args:
        data (list): list of integers representing bytes.
    Returns:
        bool: True if valid UTF-8 encoding, else False.
    """
    n_bytes = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get only the 8 least significant bits
        byte = num & 0xFF

        if n_bytes == 0:
            # Count the number of leading 1s
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # 1-byte character (starts with 0)
            if n_bytes == 0:
                continue

            # Invalid scenarios for UTF-8:
            # - n_bytes == 1 means 10xxxxxx which is invalid as a start byte
            # - n_bytes > 4 is invalid because UTF-8 max is 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False

            n_bytes -= 1
        else:
            # Check if it's a valid continuation byte (starts with 10)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            n_bytes -= 1

    return n_bytes == 0
