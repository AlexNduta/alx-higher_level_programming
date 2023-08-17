#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_elements = list(a_dictionary.keys())
    key_elements.sort()
    for key in key_elements:
        print("{}:{}".format(key, a_dictionary[key]))

