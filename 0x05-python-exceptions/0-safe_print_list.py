#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_counter = 0
    for item in range(x):
        try:
            print(my_list[item], end=" ")
            printed_counter += 1
    except IndexError:
        break

    print()
    return printed_counter
