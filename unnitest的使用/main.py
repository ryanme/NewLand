# coding: utf8
import unittest


class Mydemo(unittest.TestCase):

    def setUp(self):
        self.a=1
    def test1(self):
        print("i am test1 the value of a is {}".format(self.a))
    def test2(self):
        print("i am test2 the value of a is {}".format(self.a))
    def  test3(self):
        print("i am test3 the value of a is {}".format(self.a))


if __name__ == '__main__':
    unittest.main()