#!/usr/bin/python3

"""
This is a module for pascal_triangle.
"""


def pascal_triangle(n):
    """Return a list of lists of integers representing the Pascal’s
    triangle of n"""
    res = []
    if n <= 0:
        return res
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(res[-1][j:j + 2]))
        res.append(row)
    return res
