#!/usr/bin/python3

def safe_print_list_integers(my_list[], x=0):
    printed_item = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list(item)), end="")
            printed_item += 1
        except Exception:
            pass
        except IndexError as y:
            print("{}".format(y))
        else:
            print()
            return printed_item
