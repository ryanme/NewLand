# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/23 9:55
# @Title   : 可迭代对象
from collections.abc import Iterable, Iterator

"""
Iteration   迭代 ， 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
Iterable    可迭代对象， python例如 字符串, dict, list, tuple等
Iterator    迭代器
。
在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如Java代码：
for (i=0; i<list.length; i++) {
    n = list[i];
}
Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

"""


# 判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
def is_iterable():
    print(isinstance('abc', Iterable))
    print(isinstance('abc', Iterator))


# list实现类似Java那样的下标循环,Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
def test_enumerate():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)


# p
def makereader():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in x:
        yield i
    yield None

reader = makereader()
x = reader.__next__()
print(x)
print(isinstance(reader, Iterable))


# 练习插曲，使用迭代查找一个list中最小和最大值，并返回一个tuple：
def return_min_max(temp_list):
    temp_tuple = ()
    if temp_list:
        max = temp_list[0]
        min = temp_list[0]
        for x in temp_list:
            if x >= max:
                max = x
            if x <= min:
                min = x
        temp_tuple = (max, min)
    return temp_tuple


if __name__ == '__main__':
    # is_iterable()
    # test_enumerate()
    print(return_min_max([1, 5, 6, 22, 6, 15, 1]))
    print(return_min_max([]))


print([m + n for m in 'ABC' for n in 'XYZ'])