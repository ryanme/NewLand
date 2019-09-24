# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/23 9:55

from collections.abc import Iterator, Iterable, Generator
"""
Generator   生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
"""

L = [x * x for x in range(10)]
print(L)
print(isinstance(L, Generator))  # False
print(isinstance(L, Iterator))  # False
print(isinstance(L, Iterable))  # False

"""
创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
"""
g = (x * x for x in range(10))
print(g)
print(isinstance(g, Generator))  # True
print(isinstance(g, Iterator))  # True
print(isinstance(g, Iterable))  # True

"""
如果要一个一个打印生成器的元素，可以通过next()函数获得generator的下一个返回值。next()和__next__()效果一样
"""
print(g.__next__())
print(next(g))

"""
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象。

我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
"""
g = (x * x for x in range(10))
for n in g:
    print(n)


"""
斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易（（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到）
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n +1
    return 'done'

print(fib(5))
"""
可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了。

回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
"""

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n +1
    return 'done'

f=fib2(6)
print(f)
print(next(f))

"""
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
"""
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
print(next(o))
print(next(o))
print(next(o))
# print(next(o))  # StopIteration
"""
odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，
所以，第4次调用next(o)就报错。
"""

"""
用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，
返回值包含在StopIteration的value中：
"""

g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:%s' % x)
    except StopIteration as e:
        print('Generator return value:%s' % e.value)
        break

"""
杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：
"""


def demo2():
    yh_list = [1]
    while True:
        L = yh_list[:]
        yield yh_list[:]
        for i in range(0,len(L)-1):
            yh_list[i+1] = L[i]+L[i+1]
        yh_list.append(1)

x = demo2()
print('demo2:', next(x))
print('demo2:', next(x))
print('demo2:', next(x))
print('demo2:', next(x))