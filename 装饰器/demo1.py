# coding: utf-8
# author: ryan
# date: 2019/8/15 14:35

"""
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
"""
import time


def now():
    print('2015-3-25')

# f = now
# f()

# 函数对象有一个__name__属性，可以拿到函数的名字
# print(now.__name__)  # now
# print(f.__name__)  # now

"""
设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
"""


def print_log(func):
    def wrapper(*args, **kwargs):   # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

        print('call %s()' % func.__name__)
        return func(*args, **kwargs)    # 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
    return wrapper


@print_log  # 把@print_log放到now2()函数的定义处，相当于执行了语句：now2 = print_log(now2)
def now2():
    print('2019-01-01')
# now2()


"""
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
"""
def print_log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s, %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@print_log2('execute')
def now3():
    import time
    print(time.time())

# now3()
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的： now3 = print_log2('execute')(now3)
# 首先执行print_log2('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。


"""
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
"""
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 或者针对带参数的decorator
def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间

def print_excute_time(func):
        @functools.wraps(func)
        def metric(*args, **kwargs):
            print('%s executed in %s ms' % (func.__name__, 10.24))
            return func(*args, **kwargs)
        return metric

@print_excute_time
def fast(x, y):
    import time
    time.sleep(0.0012)
    return x + y

# print(fast(5, 6))


"""
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
再思考一下能否写出一个@log的decorator，使它既支持：
@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
"""


def log4(fn):
    if hasattr(fn, '__call__'):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print('%s begintime:%s' % (fn.__name__, time.time()))
            fn()
            print('%s endtime:%s' % (fn.__name__, time.time()))
        return wrapper
    else:
        def decortor(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print('%s begintime:%s' % (func.__name__, time.time()))
                func(*args, **kwargs)
                print('%s endtime:%s' % (func.__name__, time.time()))
                return
            return wrapper
        return decortor


# 在这里,wrapper其实是demo1的代理函数。wrapper没有return，下面调用demo1也没有return。

@log4
def demo1():
    print('It\'s demo1')

# 调用demo1相当于 demo1=log4(demo1)() 即decortor(demo1)()   (而demo1就是代理函数wrapper)
# 这边没有入参，所以只需要两层，decortor是多余，那么func就不是必须， func=None

@log4('mmb')
def demo2():
    print('It\'s demo2')

# 调用demo2相当于 demo2=log4(params)(demo2)()  即decortor(demo2(params))()       (而demo2就是代理函数wrapper)


demo1()

print('*****************')

demo2()
