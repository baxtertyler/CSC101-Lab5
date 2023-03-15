# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

import unittest
from nested import *


class TestNested(unittest.TestCase):

    def test_product(self):  # Tests the product function
        self.assertListEqual(product([[1, 2], [2, 3, 4], [-2, 5]]), [2, 24, -10])
        self.assertListEqual(product([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]), [120, 120])
        self.assertListEqual(product([[-1, 1], [-3, 3], [-5, 5], [-7, 7]]), [-1, -9, -25, -49])

