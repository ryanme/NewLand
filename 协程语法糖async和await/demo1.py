# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/10 0:45

"""
举个例子：假设有1个洗衣房，里面有10台洗衣机，有一个洗衣工在负责这10台洗衣机。那么洗衣房就相当于1个进程，洗衣工就相当1个线程。
如果有10个洗衣工，就相当于10个线程，1个进程是可以开多线程的。这就是多线程！

那么协程呢？先不急。大家都知道，洗衣机洗衣服是需要等待时间的，如果10个洗衣工，1人负责1台洗衣机，这样效率肯定会提高，
但是不觉得浪费资源吗？明明1 个人能做的事，却要10个人来做。只是把衣服放进去，打开开关，就没事做了，等衣服洗好再拿出来就可以了。
就算很多人来洗衣服，1个人也足以应付了，开好第一台洗衣机，在等待的时候去开第二台洗衣机，再开第三台，……直到有衣服洗好了，
就回来把衣服取出来，接着再取另一台的（ 哪台洗好先就取哪台，所以协程是无序的）。这就是计算机的协程！洗衣机就是执行的方法。

好了！现在来总结一下：

洗衣房 ==> 进程
洗衣工 ==> 线程
洗衣机 ==> 方法（函数）
"""
import asyncio
import time

import requests

"""
正常的函数在执行时是不会中断的，所以你要写一个能够中断的函数，就需要添加async关键。
async 用来声明一个函数为异步函数，异步函数的特点是能在函数执行过程中挂起，去执行其他异步函数，等到挂起条件（假设挂起条件是sleep(5)）
消失后，也就是5秒到了再回来执行。

await 用来用来声明程序挂起，比如异步程序执行到某一步时需要等待的时间很长，就将此挂起，去执行其他的异步程序。
await 后面只能跟异步程序或有__await__属性的对象，因为异步程序与一般程序不同。假设有两个异步函数async a，async b，a中的某一步有await，
当程序碰到关键字await b()后，异步程序挂起后去执行另一个异步b程序，就是从函数内部跳出去执行其他函数，当挂起条件消失后，不管b是否执行完，
要马上从b程序中跳出来，回到原程序执行原来的操作。如果await后面跟的b函数不是异步函数，那么操作就只能等b执行完再返回，
无法在b执行的过程中返回。如果要在b执行完才返回，也就不需要用await关键字了，直接调用b函数就行。所以这就需要await后面跟的是异步函数了。
在一个异步函数中，可以不止一次挂起，也就是可以用多个await。
"""
async def test2(i):
    r = await other_test(i)
    print(i,r)


async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(4)
    return r

url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]


loop = asyncio.get_event_loop() # 创建一个循环
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task)) # 将异步函数包装成task或者future, 监测loop.run_until_complete(asyncio.wait(task))
                                            # 来监测task运行的情况并返回结果，比如什么时候挂起，什么时候回来执行原方法等
                                            # 当所有的异步程序运行完就会返回最后结果
end = time.time()
print(end-start)    # 可以看到基本上只花了等待了的4s，三个网站不是顺序访问的，否则时间不止4s，至少12s多。
loop.close()