# coding: utf8

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FoO')


if __name__ == '__main__':
    unittest.main()