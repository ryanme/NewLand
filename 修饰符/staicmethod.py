# coding: utf8

"""
property
classmethod
staticmethod @staticmethod 静态方法只是名义上归属类管理，但是不能使用类变量和实例变量，是类的工具包
放在函数前（该函数不传入self或者cls），所以不能访问类属性和实例属性
"""


class cal:
    cal_name = "计算器"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 在cal_add函数前加上@property，使得该函数可直接调用，封装起来
    @property
    def cal_add(self):
        return self.x+self.y

    # 在cal_info函数前加上@classmethon，则该函数变为类方法，该函数只能访问到类的数据属性，不能获取实例的数据属性
    @classmethod
    # python自动传入位置参数cls就是类本身
    def cal_info(cls):
        # cls.cal_name调用类自己的数据属性
        print('这是一个%s' % cls.cal_name)

    # 静态方法 类或实例均可调用
    @staticmethod
    # 改静态方法函数里不传入self 或 cls
    def cal_test(a, b, c):
        print(a, b, c)


cl = cal(10, 11)
cl.cal_test(1, 2, 3)
print(cl.cal_add)
cl.cal_info()
print(cal.cal_name)
