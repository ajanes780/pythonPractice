import unittest
from unittest import result
import fibonacci


class TestMain(unittest.TestCase):
    def test_fibonacci(self):
        params = 21
        result = [i for i in fibonacci.fibonacci_number(params)]

        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765])

    def test_fibonacci2(self):
        params = -1
        result = [i for i in fibonacci.fibonacci_number(params)]

        self.assertEqual(result, "Please Choose a number greater then 0")


if __name__ == "__main__":
    unittest.main()
