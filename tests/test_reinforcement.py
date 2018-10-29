from unittest import TestCase

from Exercises.r1_1 import is_multiple
from Exercises.r1_2 import is_even
from Exercises.r1_3 import minmax
from Exercises.r1_4 import squares_sum


class TestReinforcement(TestCase):
    def test_is_multiple(self):
        self.assertTrue(is_multiple(4, 2))
        self.assertFalse(is_multiple(5, 3))

    def test_is_even(self):
        for k in range(2, 10, 2):
            self.assertTrue(is_even(k))
            self.assertFalse(is_even(k + 1))

    def test_minmax(self):
        min_, max_ = minmax([1, 3, 7, -10, 39, 46, 9])
        self.assertEqual(min_, -10)
        self.assertEqual(max_, 46)

    def test_squares_sum(self):
        self.assertEqual(squares_sum(4), 14)
        self.assertEqual(squares_sum(5), 30)
        self.assertEqual(squares_sum(6), 55)
