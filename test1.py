import unittest
from my_sum import sum
from fractions import Fraction


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """"
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fractions(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)
    # this test case will only pass if sum(data) raises a TypeError

    def test_bad_type(self):

        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == '__main__':
    unittest.main()


"""""
how to call on command line -v = verbose
python -m unittest test1
python3 -m unittest -v test1
python3 -m unittest discover
when multiple test files, as long as the test*.py naming pattern
you can provide the name of the directory instead by using the -s flag
and the name of the directory
python3 -m unittest discover -s tests
python3 -m unittest discover -s test1 -t src
"""
