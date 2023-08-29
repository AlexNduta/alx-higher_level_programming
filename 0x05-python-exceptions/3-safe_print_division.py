#!/usr/bin/python3

def safe_print_division(a,b):
    try:
        result = print(a/b)
    except (ZeroDivisionError, ValueError) as ep:
        print(e)
    else:
        return None
    finally:
        return result
