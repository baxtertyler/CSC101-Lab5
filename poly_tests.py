# CPE 101-01
# LAB 5: Polynomial Function Tests
# Name: Tyler Baxter
# Section: 03

import unittest
from poly import *


class TestPoly(unittest.TestCase):
    # do not delete this part, use this to compare two lists
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_poly_add2(self):  # Tests the poly_add2 function
        self.assertListEqual(poly_add2([1, 2, 3], [2, 3, 4]), [3, 5, 7])
        self.assertListEqual(poly_add2([1, 1, 1], [0, 0, 0]), [1, 1, 1])
        self.assertListEqual(poly_add2([-2,  5, -8], [1, 6, -4]), [-1, 11, -12])

    def test_poly_mult2(self):  # Tests of poly_mult2 function
        self.assertListEqual(poly_mult2([2, 1], [2, 1]), [4, 4, 1])
        self.assertListEqual(poly_mult2([3, 1], [2, 1]), [6, 5, 1])
        self.assertListEqual(poly_mult2([2, 2], [3, 5]), [6, 16, 10])


if __name__ == '__main__':
    unittest.main()
