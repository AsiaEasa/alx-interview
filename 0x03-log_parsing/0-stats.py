#!/usr/bin/python3
"""
parsing function
"""
import sys


count = {
    "size": 0,
    "lines": 1
}

sCode = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def Codes():
    """
    function to print the codes and the number of ocurrence
    """
    print("File size: {}".format(count["size"]))

    for key in sorted(sCode.keys()):

        if sCode[key] != 0:
            print("{}: {}".format(key, sCode[key]))


def CodeSize(listData):
    """
    count the codes and file size
    """

    count["size"] += int(listData[-1])

    if listData[-2] in sCode:

        sCode[listData[-2]] += 1


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                CodeSize(line.split(" "))
            except:
                pass
            if count["lines"] % 10 == 0:
                Codes()
            count["lines"] += 1
    except KeyboardInterrupt:
        Codes()
        raise
    Codes()
