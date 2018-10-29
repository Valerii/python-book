"""
Write a short Python function that takes a positive integer n
and returns the sum of the squares of all the odd positive integers smaller than n.
"""


def sum_of_odd(n):
    return sum(k for k in range(1, n, 2))
