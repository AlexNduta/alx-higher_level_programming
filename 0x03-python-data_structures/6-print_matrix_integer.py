#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for n in matrix:
            print(" ".join("{:d}".format(num)for num in n))
