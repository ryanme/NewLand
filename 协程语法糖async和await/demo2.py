# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/18 17:12

import asyncio
import functools

"""
所谓「异步 IO」，就是你发起一个 IO 操作，却不用等它结束，你可以继续做其他事情，当它结束时，你会得到通知。
Asyncio 是并发（concurrency）的一种方式。对 Python 来说，并发还可以通过线程（threading）和多进程（multiprocessing）来实现。
Asyncio 并不能带来真正的并行（parallelism）。当然，因为 GIL（全局解释器锁）的存在，Python 的多线程也不能带来真正的并行。
可交给 asyncio 执行的任务，称为协程（coroutine）。一个协程可以放弃执行，把机会让给其它协程（即 yield from 或 await）。`
"""


# 定义协程
async def do_some_work(x):
    print("Waiting " + str(x))
    await asyncio.sleep(x)


# print(asyncio.iscoroutinefunction(do_some_work)) # True

# 调用协程函数，协程并不会开始运行，只是返回一个协程对象，可以通过 asyncio.iscoroutine 来验证：
# print(asyncio.iscoroutine(do_some_work(3)))

# 要让这个协程对象运行的话，有两种方式：
# * 在另一个已经运行的协程中用 `await` 等待它
# * 通过 `ensure_future` 函数计划它的执行

loop = asyncio.get_event_loop()
# # run_until_complete 是一个阻塞（blocking）调用，直到协程运行结束，它才返回。
# loop.run_until_complete(do_some_work(3)) # 等同于loop.run_until_complete(asyncio.ensure_future(do_some_work(3)))


# 回调
# 假如协程是一个 IO 的读操作，等它读完数据后，我们希望得到通知，以便下一步数据的处理。这一需求可以通过往 future 添加回调来实现。


def done_callback(futu):
    print('我是回调函数')

# loop2 = asyncio.get_event_loop()
#
# futu = asyncio.ensure_future(do_some_work(3))
# futu.add_done_callback(done_callback)
#
# loop2.run_until_complete(futu)


# 多个协程
# 实际项目中，往往有多个协程，同时在一个 loop 里运行。为了把多个协程交给 loop，需要借助 asyncio.gather 函数。

# loop.run_until_complete(asyncio.gather(do_some_work(1), do_some_work(3)))
# 或者先把协程存在列表里：
# coros = [do_some_work(1), do_some_work(3)]
# loop.run_until_complete(asyncio.gather(*coros))
# 这两个协程是并发运行的，所以等待的时间不是 1 + 3 = 4 秒，而是以耗时较长的那个协程为准。

# 也可以传futures给gather
# futus = [asyncio.ensure_future(do_some_work(1)),
#              asyncio.ensure_future(do_some_work(3))]
# loop.run_until_complete(asyncio.gather(*futus))


# run_forever
# coro = do_some_work(3)
# asyncio.ensure_future(coro)

# loop.run_forever()
# 三秒钟过后，future 结束，但是程序并不会退出。run_forever 会一直运行，直到 stop 被调用,
# run_forever 不返回，stop 永远也不会被调用。所以，只能在协程中调 stop

async def do_some_work2(loop, x):
    print('Waiting ' + str(x))
    await asyncio.sleep(x)
    print('Done')
    loop.stop()

# asyncio.ensure_future(do_some_work2(loop, 3))
# loop.run_forever()
# 假如有多个协程在 loop 里运行,第二个协程没结束，loop 就停止了——被先结束的那个协程给停掉的。
# 要解决这个问题，可以用 gather 把多个协程合并成一个 future，并添加回调，然后在回调里再去停止 loop。

# def done_callback2(loop, futu):
#     loop.stop()
# futus = asyncio.gather(do_some_work2(loop, 1), do_some_work2(loop, 3))
# futus.add_done_callback(functools.partial(done_callback2, loop))
# loop.run_forever()
# 其实这基本上就是 run_until_complete 的实现了，run_until_complete 在内部也是调用 run_forever。




# 以上示例都没有调用 loop.close，好像也没有什么问题。所以到底要不要调 loop.close 呢？
# 简单来说，loop 只要不关闭，就还可以再运行。：
# loop.run_until_complete(do_some_work(1))
# loop.run_until_complete(do_some_work(3))
# loop.close()
# 但是如果关闭了，就不能再运行了：
# loop.run_until_complete(do_some_work(1))
# loop.close()
# loop.run_until_complete(do_some_work(3))
# 建议调用 loop.close，以彻底清理 loop 对象防止误用。




# asyncio.gather 和 asyncio.wait 功能相似。
# coros = [do_some_work(1), do_some_work(3)]
# loop.run_until_complete(asyncio.wait(coros))


# Timer
# C++ Boost.Asio 提供了 IO 对象 timer，但是 Python 并没有原生支持 timer，不过可以用 asyncio.sleep 模拟。

async def timer(x, cb):
    futu = asyncio.ensure_future(asyncio.sleep(x))
    futu.add_done_callback(cb)
    await futu

t = timer(3, lambda futu: print('Done'))
loop.run_until_complete(t)