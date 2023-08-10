#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total_sum = 0
    for argument in sys.argv[1:]:
        total_sum = total_sum + int(argument)
    print(total_sum)
