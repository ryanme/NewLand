# coding: utf8

from assertpy import assert_that


def test_something():
    assert_that(1 + 2).is_equal_to(1)
    assert_that('foobar')\
        .is_length(6)\
        .starts_with('foo')\
        .ends_with('bar')
    assert_that(['a', 'b', 'c'])\
        .contains('a')\
        .does_not_contain('x')


print(test_something())