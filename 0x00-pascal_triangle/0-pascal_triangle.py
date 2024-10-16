#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    """
    Function that returns a list of lists representing
    Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])  # Sum the two numbers directly above
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
