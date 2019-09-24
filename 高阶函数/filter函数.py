# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/5 15:07


"""
和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素。
filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
"""


# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', 'B', '', None, 'C', '  '])))


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(s):
    flag = True
    length = len(str(s))
    num = int(length/2)
    if not length % 2 == 0:
        num = num+1
    for i in range(0, num-1):
        if not str(s)[i] == str(s)[length-1-i]:
            flag = False
            continue
    return s and flag == True


print(list(filter(is_palindrome, [1232, 909, 12321, 2678762])))