# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/3 9:36
import asyncio

from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()
async def get_pythonorg():
    r = await asession.get('http://qq.com')
    print(r.text)
    return r

async def get_reddit():
   r = await asession.get('http://baidu.com/')
   print(r.url)
   return r

async def get_google():
   r = await asession.get('http://souhu.com/')
   print(dir(r.html))
   return r

async def demo1(x):
    print("Wait"+str(x))
    await asyncio.sleep(x)

# print(asyncio.iscoroutinefunction(get_pythonorg))
# print(asyncio.iscoroutine(demo1(1)))


# loop = asyncio.get_event_loop()

# loop.run_until_complete(demo1(5))
#
# loop.run_until_complete(asyncio.ensure_future(demo1(3)))

def done_callback(loop, futu):
    loop.stop()
    print('Done')

# futu = asyncio.ensure_future(demo1(3))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)

# loop = asyncio.get_event_loop()
# coros = [get_pythonorg(), get_reddit(), get_google()]
# futu = asyncio.gather(*coros)
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)

# loop.run_until_complete(asyncio.gather(*coros))

a = 1
b = 2
c = a
print(a is b)
print(a is c)
print(id(a), id(b), id(c))