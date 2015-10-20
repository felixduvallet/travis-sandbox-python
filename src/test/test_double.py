__author__ = 'felixd'

import unittest

from double import double

class TestCase(unittest.TestCase):
    def test_four(self):
        ret = double(4)
        self.assertEqual(8, ret)

if __name__ == '__main__':
    unittest.main()
