#!/usr/bin/python3
"""
Parsing function to count file sizes and HTTP status codes from log data
"""
import sys


COUNT = {
    "size": 0,
    "lines": 1
}

SCODE = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def codes():
    """
    Function to print the codes and the number of occurrences
    """
    print("File size: {}".format(COUNT["size"]))

    for key in sorted(SCODE.keys()):

        if SCODE[key] != 0:
            print("{}: {}".format(key, SCODE[key]))


def code_size(list_data):
    """
    Count the codes and file size
    """

    COUNT["size"] += int(list_data[-1])

    if list_data[-2] in SCODE:

        SCODE[list_data[-2]] += 1


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                code_size(line.split(" "))
            except:
                pass
            if COUNT["lines"] % 10 == 0:
                codes()
            COUNT["lines"] += 1
    except KeyboardInterrupt:
        codes()
        raise
    codes()
