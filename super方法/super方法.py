# coding: utf8

"""
涉及到多重继承的时候，使用super()可以保证公共父类只被执行一次
super是一个类， 不是方法也不是关键字
提供一个 MRO 以及一个 MRO 中的类 C ， super() 将返回一个从 MRO 中 C 之后的类中查找方法的对象。
"""


class Foo:
    def bar(self, message):
        print(message)


class FooChild(Foo):
    def bar(self, message):
        Foo.bar(self, message)
        print('1111111111')

# FooChild().bar('12')


class FooChild2(Foo):
    def __init__(self):
        super().__init__()

    def bar(self, message):
        print('我就呵呵了')

# FooChild2().bar('123')


# 单继承
class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        # print('self is {0} @A.add'.format(self))
        # [A, object]
        print('A1', self.n)
        self.n += m
        print('A2', self.n)


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        # print('self is {0} @B.add'.format(self))
        # [B, C, A, object]
        print('B1', self.n)
        super().add(m)  # super().add(m) 调用父类方法 def add(self, m) 时, 此时父类中 self 并不是父类的实例而是子类的实例, 所以 b.add(2) 之后的结果是 5 而不是 4 。
        print('B2', self.n)
        self.n += 3
        print('B3', self.n)


# b=B()
# b.add(2)
# print(b.n)


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        # print('self is {0} @C.add'.format(self))
        print('C1', self.n)
        # [C, A, object]
        super().add(m)
        print('C2', self.n)
        self.n += 4
        print('C3', self.n)


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('D1', self.n)
        # print('self is {0} @D.add'.format(self))
        # [D, B, C, A, object]
        super().add(m)
        print('D2', self.n)
        self.n += 5
        print('D3', self.n)


d = D()
d.add(2)
# print(d.n)


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChilddd(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
        super(FooChilddd, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChilddd, self).bar(message)
        print('Child bar fuction')
        print(self.parent)


# if __name__ == '__main__':
#     fooChild = FooChilddd()
#     fooChild.bar('HelloWorld')


class ChildInfo:
    def __init__(self):
        self.age = 18

    def get_age(self, name):
        print('%s 今年 %s' % (name, self.age))


class Childchild(ChildInfo):
    def __init__(self):
        super().__init__()
        self.age = 16
        self.sex = '男'

    def get_info(self, name):
        self.get_age(name)
        print('%s 今年 %s, 性别 %s' % (name, self.age, self.sex))

# cc = Childchild()
# cc.get_info('小明')