# coding: utf8
"""
当函数的参数不确定时，可以使用*args和 **kwargs，*args 没有key值，**kwargs 有key值。

args是一个tuple, *args可传字符串，数字，布尔型，列表，元祖和字典等。
"""


def args_demo(param1, *args):
    print("params1 is %s" % param1)
    # print(type(args))
    # print(args[0])
    index = 1
    for value in args:
        print("the " + str(index) + " is:" + str(value))
        index +=1
    print("\t")


args_demo("param", 1, 2)


args_demo("第一个参数个", ["1", "L", "p"], ["2", "3", "4"])

args_demo("第一个参数个", 2, 3, (1, 2), True)

args_demo("第一个参数个", {"a": "1", "b": "2"}, "2", 1)


def args_demo2(*args):
    print(type(args))
    print(args)
    print("\t")


args_demo2(*(1, 2, 3))
args_demo2((1, 2, 3))
args_demo2(1, 2, 3)