#!/usr/bin/python3
import sys
if __name___ == "__main__":
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argumnet:")
    else:
        print("{} arguments:".format(count))
    for x in range(count):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
