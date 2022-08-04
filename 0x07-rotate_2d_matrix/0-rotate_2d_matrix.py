#!/usr/bin/python3
"""
Code 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """for this matrix to be rotated in 90 deg clockwise
it first needs to be transposed and then the first and the last
index of the transposed column of each row witll be swapped

A = [[1,2,3],        Atran = [[1,4,7],     A90 = [[7,4,1],
     [4,5,6],                 [2,5,8],            [8,5,2],
     [7,8,9]]                 [3,6,9]]            [9,6,3]]

time-complexity = O(n2)
space-complexity = O(1)
"""
    no_of_rows = len(matrix)
    # since it's n * n matrix, rows == columns
    no_of_columns = no_of_rows

    for i in range(no_of_rows):
        for j in range(i):
            if i != j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

    for i in range(no_of_rows):
        for j in range(int(no_of_columns/2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][no_of_columns-j-1]
            matrix[i][no_of_columns-j-1] = temp
