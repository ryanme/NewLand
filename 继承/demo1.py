# coding: utf8
"""
子类继承多个父类
"""

class A:
    def __init__(self):
        print("aaa")

class B:
    def __init__(self):
        print("bbb")

class C1(A,B):
    pass

class C2(B,A):
    pass

if __name__=="__main__":
    print("A--->",)
    a = A()
    print("B--->",)
    b = B()
    print("C1(A,B)--->",)
    c1 = C1()
    print("C2(B,A)--->",)
    c2 = C2()


"""
#运行结果

A---> aaa
B---> bbb
C1(A,B)---> aaa
C2(B,A)---> bbb
"""

"""
类C1继承了两个类A，B；类C2也继承了两个类，只不过书写顺序有点区别(B,A)。从运行结果可以看出，当子类继承多个父类的时候，
对于构造函数__init__()，只有第一个能够被继承，第二个就等掉了。所以，一般情况下，不会在程序中做关于构造函数的同时多个继承
"""

"""
在Python中，可以進行多重繼承，這個時候要注意搜尋的順序，
是從子類別開始，接著是同一階層父類別由左至右搜尋，
再至更上層同一階層父類別由左至右搜尋，直到達到頂層為止。
"""

class A(object):
    def method1(self):
        print('A.method1')

    def method2(self):
        print('A.method2')

class B(A):
    def method3(self):
        print('B.method3')

class C(A):
    def method2(self):
        print('C.method2')

    def method3(self):
        print('C.method3')

class D(B, C):
    def method4(self):
        print('C.method4')

d = D()
d.method4() # 在 D 找到，C.method4
d.method3() # 以 D->B 順序找到，B.method3
d.method2() # 以 D->B->C 順序找到，C.method2
d.method1() # 以 D->B->C->A 順序找到，A.method1


