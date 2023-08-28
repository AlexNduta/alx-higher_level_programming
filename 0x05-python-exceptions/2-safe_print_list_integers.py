#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_item = 0
    for item in my_list[:x]:
        try:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                printed_item += 1
        except (ValueError, TypeError):
            continue
    print()
    return printed_item
