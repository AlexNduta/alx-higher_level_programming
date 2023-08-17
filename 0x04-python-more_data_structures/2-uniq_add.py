#!/usr/bin/python3

def uniq_add(my_list=[]):
    converted = set(my_list)
    reconverted = list(converted)
    total_sum = 0
    for unique in reconverted:
        total_sum += unique
    return total_sum
