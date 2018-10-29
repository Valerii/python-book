import math

"""
Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns:
the smallest and largest numbers, in the form of a tuple of length two.
Do not use the built-in functions min or max in implementing your solution.
"""


def minmax(data):
    min = math.inf
    max = -math.inf

    for n in data:
        min = n if n < min else min
        max = n if n > max else max

    return (min, max)
