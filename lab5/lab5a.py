#!/usr/bin/python3

import sys

from reversemath import ReverseFloat

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            f1 = ReverseFloat(float(sys.argv[1]))
            f2 = ReverseFloat(float(sys.argv[2]))
            print(f"{f1} + {f2} = {f1 + f2}")
            print(f"{f1} - {f2} = {f1 - f2}")
            print(f"{f1} * {f2} = {f1 *  f2}")
            print(f"{f1} / {f2} = {f1 / f2}")
        except:
            raise Exception("Invalid Values.")
    else:
        raise Exception("Invalid number of command line arguments.")
