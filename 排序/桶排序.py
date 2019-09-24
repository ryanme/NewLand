# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/30 16:05
"""
优点，快
缺点，耗资源
"""
#!/usr/bin/env python
#-*- coding:utf8 -*-


list_a = [21, 16, 19, 7, 2, 3, 5, 5]
# temp_dict = {}
#
# for a in range(0, len(list_a)):
#     temp_dict[a] = list_a[a]
#
# length = len(temp_dict)
length = len(list_a)
temp = ""

for i in range(0, length):
    for j in (0, length-1):
        if list_a[i]>list_a[j]:
            list_a[i] = temp
            temp = list_a[j]
            list_a[i] = list_a[j]

print(list_a)
