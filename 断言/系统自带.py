# coding: utf8

assert 1+1 == 2
assert isinstance('Hello', str)
assert isinstance('Hello', int)

# 一旦断言发生false的情况就跳出了，下面的语句就不会打印
# 且在程序中不会告诉你哪里错了
print(111)