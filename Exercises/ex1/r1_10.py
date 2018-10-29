"""
What parameters should be sent to the range constructor, to produce a range with values:
8, 6, 4, 2, 0, −2, −4, −6, −8?
"""


def get_odd8_to_minue8():
    return [k for k in range(8, -9, -2)]
