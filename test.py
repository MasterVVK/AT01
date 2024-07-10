# test.py

import unittest
from main import remainder


class TestRemainderFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 4), 0)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), -1)
        self.assertEqual(remainder(10, -3), 1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 3), 0)
        self.assertEqual(remainder(0, -3), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_both_zero(self):
        with self.assertRaises(ValueError):
            remainder(0, 0)


if __name__ == '__main__':
    unittest.main()
