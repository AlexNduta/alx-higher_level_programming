#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # define an empty list to hold each element
    squared_matrix = []
    for row in matrix:  # iterate through each row in the matrix
        # iterate through the each i    tem in the row and square it
        squared_row = [item ** 2 for item in row]
        squared_matrix.append(squared_row)
    return squared_matrix
