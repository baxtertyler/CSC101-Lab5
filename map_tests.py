# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

import unittest
from map import *


class TestMap(unittest.TestCase):

    def test_cube_all(self):  # This tests the cube_all function
        self.assertListEqual(cube_all([1, 2, 3]), [1, 8, 27])
        self.assertListEqual(cube_all([2, 2, 3]), [8, 8, 27])
        self.assertListEqual(cube_all([0, 2, 4]), [0, 8, 64])

    def test_add_n_to_all(self):  # This tests the add_n_to_all function
        self.assertListEqual(add_n_to_all([1, 2, 3, 4, 5], 5), [6, 7, 8, 9, 10])
        self.assertListEqual(add_n_to_all([2, 3, 4, 5], 10), [12, 13, 14, 15])
        self.assertListEqual(add_n_to_all([-5, 0, 5], 5), [0, 5, 10])

    def test_div_by_5_all(self):  # This tests the div_all_by_5 function
        self.assertListEqual(div_by_5_all([5, 6, 10, 11]), [True, False, True, False])
        self.assertListEqual(div_by_5_all([10, 15, 1, 2]), [True, True, False, False])
        self.assertListEqual(div_by_5_all([-5, 0, 5]), [True, True, True])
