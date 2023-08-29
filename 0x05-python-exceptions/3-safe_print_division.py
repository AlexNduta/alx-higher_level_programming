#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        reult = a/b
    except (ZeroDivisionError, ValueError) as ep:
        print(ep)
    else:
        return None
    finally:
        return result
