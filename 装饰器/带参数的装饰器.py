# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/9 22:25

"""
紧接着第一个
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction()


@a_new_decorator('wo cao')
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
"""

"""
因为a_function_requiring_decoration()=a_new_decorator(a_function_requiring_decoration)()
a_new_decorator(a_function_requiring_decoration) 返回的是函数对象wrapTheFunction,执行a_function_requiring_decoration()
就等于执行wrapTheFunction()



装饰器本质上是wrapTheFunction代理了a_function_requiring_decoration方法，所以需要参数，需要在wrapTheFunction方法传递变量，
wrapTheFunction(*args, **kwargs)，代理函数也就是原来的函数执行func(*args, **kwargs)，然后跟上面一样，传递函数对象wrapTheFunction
最后返回decortor@a_new_decorator("just do it") 等价于 @decorator，最外层方法只用来接收参数
"""
from functools import wraps


# 继续写
def a_new_decorator(hehe):
    def decortor(func):
        @wraps(func)
        def wrapTheFunction(*args, **kwargs):
            print("I am doing some boring work before executing a_func()")
            print(hehe)
            print("I am doing some boring work after executing a_func()")
            return func(*args, **kwargs)
        return wrapTheFunction
    return decortor


@a_new_decorator('just do it')
def demo1():
    print("demo1 do something")


demo1()

"""
@a_new_decorator('just do it')相当于a_new_decorator('just do it')(demo1)
执行demo1()就相当于a_new_decorator('just do it')(demo1)()
"""
