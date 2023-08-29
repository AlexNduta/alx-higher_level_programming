#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        return print("{:d}".format(result))
