#!/usr/bin/python3
""" 
This is a function that divides all elements of a mattix
The funtion takes a matrix and the value to divide the matrix as a parameter
The function returns a new matrix of the values got from dividing the matrix
"""


def matrix_divided(matrix, div):
    new_matrix = []
    reference_length = len(matrix[0]) #the length(size) of the first row
    if not isinstance(div, (int, float)): #check if div is an int or float
        raise TypeError("div must be a number")
    elif div ==0:
        raise ZeroDivisionError("division by zero")

    #loop through the rows of our ,matrix
    for row in matrix:
        if len(row) != reference_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
            dived_item = item/ div
            new_row.append(round(divided_item, 2))
        new_matrix.append(new_row)
    return new_matrix

