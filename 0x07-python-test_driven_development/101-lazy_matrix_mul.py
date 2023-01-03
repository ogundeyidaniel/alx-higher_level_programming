#!/usr/bin/python3

"""
LazyMatrixMul module
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    Args:
        m_a (list[list[int/float]]): first matrix
        m_b (list[list[int/float]]): second matrix
    Raises:
        TypeError: if 'm_a' or 'm_b' is not a list
        TypeError: if 'm_a' or 'm_b' is not a list of lists
        ValurError: if 'm_a' or 'm_b' is an empty list
        TypeError: if 'm_a' or 'm_b' contain orther than number
        ValueError: If 'm_a' and 'm_b' not compatible for multiplication
    Returns:
        [[int/floats]]: list of lists
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if len(m_a) is 0 or all(len(row) is 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0 or all(len(row) is 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if not all(all(type(e) in (int, float) for e in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(type(e) in (int, float) for e in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return np.dot(m_a, m_b)
