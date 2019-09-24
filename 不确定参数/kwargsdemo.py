# coding: utf8
"""
当函数的参数不确定时，可以使用*args和 **kwargs，*args 没有key值，**kwargs 有key值。

kwargs是一个tuple, *args可传字符串，数字，布尔型，列表，元祖和字典等。
"""


# def kwargs_demo(**kwargs):
#
#     for key in kwargs:
#         print("key is %s, value is %s" % (key, kwargs[key]))
#     print("\t")
#
#
# kwargs_demo(**{"X": "1", "y": "2"})
#
# kwargs_demo(x=1, y=2)

# kwargs_demo({"X": "1", "y": "2"})


def kwargs_demo2(*args, **kwargs):
    print(args)
    for key in kwargs:
        print("key is %s, value is %s" % (key, kwargs[key]))
    print("\t")


kwargs_demo2((1), 2, 3,  **{"X": "1", "y": "2"})

kwargs_demo2((1, 2), 3,  x=1, y=2)

kwargs_demo2(*(1, 2, 3), x=1, y=2)

kwargs_demo2(*(1, 2, 3),  **{"X": "1", "y": "2"})