#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a/b
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        if result != None:
            print("{:1f}".format(result))
        else:
            print("None")
    return result
