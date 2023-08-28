#!/usr/bin/python3

def safe_print_list_integers(my_list[], x=0):
    printed_item = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int)
            print("{:d}".format(item), end="")
            printed_item += 1
    except Exception as e:
        print(e)
    print()
    return printed_item