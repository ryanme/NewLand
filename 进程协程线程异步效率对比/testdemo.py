# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/3 14:04
import time
import requests

# 多进程
from multiprocessing import Process

# 多线程
from threading import Thread

# 异步
import asyncio
# 协程
import aiohttp

class TestDemo:

    def __init__(self):
        self.urls = ['http://127.0.0.1:7777/testdemo' for _ in range(10)]

    def get_html_text(self, url):
        response = requests.get(url)
        return response.text

    async def get_html_text_by_async(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                return text

    # 单进程
    def single_process(self):
        start = time.time()
        for url in self.urls:
            result = self.get_html_text(url)
            print(result)
        end = time.time()
        print('【单进程单线程耗时:%s】' % (end-start))

    # 多进程
    def multi_process(self):
        start = time.time()
        processes = []
        for url in self.urls:
            p = Process(target=self.get_html_text, args=(url,))
            processes.append(p)
            p.start()
        for p in processes:
            p.join()
            print('Hello!')
        end = time.time()
        print('【多进程并行耗时:%s】' % (end-start))

    # 多线程
    def multi_threads(self):
        start = time.time()
        threads = []
        for url in self.urls:
            t = Thread(target=self.get_html_text, args=(url,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
            print('Hello!')
        end = time.time()
        print('【多线程并行耗时:%s】' % (end-start))

    # 协程+异步
    def async_aio(self):
        start = time.time()
        tasks = [asyncio.ensure_future(self.get_html_text_by_async(url)) for url in self.urls]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(tasks))
        for task in tasks:
            print(task.result())
        end = time.time()
        print('【协程 ++ 异步】耗时：%s 秒' % (end - start))


if __name__ == '__main__':
    td = TestDemo()
    td.single_process()
    td.multi_process()
    td.multi_threads()
    td.async_aio()