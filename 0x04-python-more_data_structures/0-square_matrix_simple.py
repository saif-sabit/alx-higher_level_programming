#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret_list = matrix.copy()
    for i in  range (len(matrix)):
        ret_list[i] = list(map(lambda x: x**2, matrix[i]))

    return ret_list
