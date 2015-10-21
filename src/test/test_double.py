__author__ = 'felixd'

import unittest

from double import double

class TestCase(unittest.TestCase):

    def test_four(self):
        ret = double(4)
        self.assertEqual(8, ret)

    def test_two(self):
        ret = double(2)
        self.assertEqual(4, ret)

    def test_bad_math(self):
        ret = double(3)
        self.assertEqual(4, ret)

if __name__ == '__main__':
    unittest.main()
