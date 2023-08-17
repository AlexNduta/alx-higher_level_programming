#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_elements = list(a_dictionary.keys())

    for key in sorted(a_dictionary.keys()):
        print("{}:{}".format(key, a_dictionary[key]))
