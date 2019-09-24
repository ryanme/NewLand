# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/9/18 20:17

from aiohttp import ClientSession
import asyncio
"""
简单学习后，写一个demo，给出一组关键词，利用协程进行搜索。
requests是同步的库，如果想异步的话需要引入aiohttp
"""

keyword_list = ['python', 'java', 'c']

tasks = []


async def visit_baidu(keyword):
    async with ClientSession() as session:
        url = "https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isid=E924D87D74D80393&wd=" + keyword + "&rsv_spt=1&rsv_iqid=0x8d3051b2000ee397&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_dl=ib&inputT=2258&rsv_sug4=2686&rsv_sid=1429_21108_20698_29523_29521_29721_29567_29221_26350_22158&_ss=1&clist=&hsug=&f4s=1&csor=4&_cr1=23000"
        async with session.get(url) as response:
            response = await response.read()
            print(response)
            return 'hehe'   # 返回信息

def run():
    for keyword in keyword_list:
        task = asyncio.ensure_future(visit_baidu(keyword))
        tasks.append(task)
    result = loop.run_until_complete(asyncio.gather(*tasks))    # 搜集返回信息
    print(result)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))