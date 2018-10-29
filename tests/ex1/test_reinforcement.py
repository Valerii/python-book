from unittest import TestCase

from Exercises.ex1.r1_1 import is_multiple
from Exercises.ex1.r1_10 import get_odd8_to_minue8
from Exercises.ex1.r1_2 import is_even
from Exercises.ex1.r1_3 import minmax
from Exercises.ex1.r1_4 import squares_sum
from Exercises.ex1.r1_6 import sum_of_odd
from Exercises.ex1.r1_9 import get_50_60_70_80


class TestReinforcement(TestCase):
    def test_is_multiple(self):
        self.assertTrue(is_multiple(4, 2))
        self.assertFalse(is_multiple(5, 3))

    def test_is_even(self):
        for k in range(2, 10, 2):
            self.assertTrue(is_even(k))
            self.assertFalse(is_even(k + 1))

    def test_min_max(self):
        min_, max_ = minmax([1, 3, 7, -10, 39, 46, 9])
        self.assertEqual(min_, -10)
        self.assertEqual(max_, 46)

    def test_squares_sum(self):
        self.assertEqual(squares_sum(4), 14)
        self.assertEqual(squares_sum(5), 30)
        self.assertEqual(squares_sum(6), 55)

    def test_sum_odd(self):
        self.assertEqual(sum_of_odd(1), 0)
        self.assertEqual(sum_of_odd(2), 1)
        self.assertEqual(sum_of_odd(3), 1)
        self.assertEqual(sum_of_odd(4), 4)
        self.assertEqual(sum_of_odd(5), 4)
        self.assertEqual(sum_of_odd(6), 9)
        self.assertEqual(sum_of_odd(7), 9)

    def test_string_index(self):
        s = 'tests!!'
        k = -3
        j = -k
        self.assertNotEqual(s[k], s[j])

    def test_range_param(self):
        self.assertEqual(get_50_60_70_80(), [50, 60, 70, 80])
        self.assertEqual(get_odd8_to_minue8(), [8, 6, 4, 2, 0, -2, -4, -6, -8])
