# coding: utf8

from ptest.decorator import *
from ptest.assertion import *


@TestClass()
class TestCases:

    @Test()
    def test1(self):
        actual = 'foo'
        expected = 'bar'
        assert_that(expected).is_equal_to(actual)
