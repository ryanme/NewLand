# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/23 9:55
# @Title   : 迭代器

from collections.abc import Iterable, Iterator

"""
Iterator    迭代器

可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
可以使用isinstance()判断一个对象是否是Iterator对象
"""
print(isinstance([], Iterable))  # True
print(isinstance((x for x in range(10)), Iterator))     # True
print(isinstance([], Iterator))     # False


# list、dict、str虽然是Iterable，却不是Iterator
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter([]), Iterator))   # True
print(isinstance(iter('abc'), Iterator))   # True


# 为什么list、dict、str等数据类型不是Iterator？
"""
因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
"""
print(x for x in range(10))  # <generator object <genexpr> at 0x034C0DF0>
print(dir(x for x in range(10)))    # 具有__next__方法
"""
小结：
凡是可作用于for循环的对象都是Iterable类型
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
"""