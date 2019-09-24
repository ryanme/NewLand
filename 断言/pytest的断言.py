# coding: utf8

import pytest

"""
这个框架对python自带的断言做了处理，如果断言失败，那么框架本身会尽可能多地提供断言失败的原因
"""
def test_case():
    expected = "Hello"
    actual = "hello"
    assert expected == actual


if __name__ == "__main__":
    pytest.main()