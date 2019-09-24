# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/9 22:24

"""
第一个装饰器
"""
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
#
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration()

"""
以上等同于
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()

@写法是python中的语法糖    
"""
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()


a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

print(a_function_requiring_decoration.__name__)    #  wrapTheFunction
"""
可以看到方法名是wrapTheFunction，而不是a_function_requiring_decoration，这里的函数被warpTheFunction替代了。
它重写了我们函数的名字和注释文档(docstring)，因为本质上，装饰器是代理了a_function_requiring_decoration。在装饰器中取名是
wrapTheFunction，Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps
"""

from functools import wraps


def b_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@b_new_decorator
def b_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")


print(b_function_requiring_decoration.__name__)  # b_function_requiring_decoration

