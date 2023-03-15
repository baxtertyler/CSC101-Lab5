# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

import unittest
from filter import *


class TestFilter(unittest.TestCase):

    def test_are_even(self):  # Tests the are_even function
        self.assertListEqual(are_even([1, 2, 3, 4]), [2, 4])
        self.assertListEqual(are_even([1, 2, 3, 4, 6, 8]), [2, 4, 6, 8])
        self.assertListEqual(are_even([-10, 0, 10]), [-10, 0, 10])

    def test_remove_duplicates(self):  # Tests the remove_duplicates function
        self.assertListEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertListEqual(remove_duplicates([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), [1])
        self.assertListEqual(remove_duplicates(["x", "x", "y", 1, "z", "y"]), ["x", "y", 1, "z"])

    def test_are_divisible_by_n(self):  # Tests the are_divisible_by_n function
        self.assertListEqual(are_divisible_by_n([2, 3, 4, 5, 6], 2), [2, 4, 6])
        self.assertListEqual(are_divisible_by_n([1, 4, 6, 9, 12, 17], 3), [6, 9, 12])
        self.assertListEqual(are_divisible_by_n([1, 4, 6, 9, 12, 17], 4), [4, 12])
