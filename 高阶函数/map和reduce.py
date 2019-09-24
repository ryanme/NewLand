# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/5 13:53


"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
"""

# 比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上
def f(x):
    return x*x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(list(r))

# 把这个list所有数字转为字符串
t = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(t)
print(list(t))


"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""

# 对一个序列求和，就可以用reduce实现
from functools import reduce
def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))  # add(add(add(add(1,3),5),7),9)


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x*10+y


print(reduce(fn, [1, 3, 5, 7, 9]))  # fn(fn(fn(fn(1,3),5),7),9)


# 对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


# 整理成一个str2int的函数,
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


# 用lambda函数进一步简化
def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
"""

def upperfirsthracter(string):
    return string[0].upper()+string[1:].lower()


m = map(upperfirsthracter, ['adam', 'LISA', 'barT'])
print(m)
print(list(m))


"""
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
"""


def prod(list):
    def ff(x, y):
        return x*y
    prod = reduce(ff, list)
    return prod


print(prod([2, 5, 6]))

"""
利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
"""
def str2float(string):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    left_string = string.split('.')[0]
    right_string = string.split('.')[1]

    lefter = reduce(lambda x, y: x*10+y, map(lambda s: digits[s], left_string))
    righter = reduce(lambda x, y: x*10+y, map(lambda s: digits[s], right_string))/(10**len(right_string))
    return lefter+righter


print(str2float('123.456'))

