# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/21 19:16

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

"""
pyppeteer是一款支持Chromium 和 Chrome 无界面访问的工具，适合js ajax动态加载的页面
"""

class PyppeteerDemo:

    async def demo1(self):
        """
        js 渲染的页面，获取源码
        :return:
        """
        broweser = await launch()
        page = await broweser.newPage()  # 相当于浏览器中新建了一个选项卡，同时新建了一个 Page 对象
        await page.goto('http://quotes.toscrape.com/js/')   # 相当于在浏览器中输入了这个 URL，浏览器跳转到这个页面加载
        doc = pq(await page.content())  # 前浏览器页面的源代码
        print('Quotes:', doc('.quote').length)
        print(doc)
        await broweser.close()

    async def demo2(self):
        """
        模拟网页截图，保存 PDF，执行自定义的 JavaScript 获得特定的内容
        :return:
        """
        browser = await launch()
        page = await browser.newPage()
        await page.goto('http://quotes.toscrape.com/js/')
        await page.screenshot(path='example.png')   # 完成了网页截图保存
        await page.pdf(path='example.pdf')  # 网页导出 PDF 保存
        # 执行 JavaScript 并返回对应数据
        dimensions = await page.evaluate('''() => { 
              return {
                  width: document.documentElement.clientWidth,
                  height: document.documentElement.clientHeight,
                  deviceScaleFactor: window.devicePixelRatio,
              }
          }''')

        print(dimensions)
        # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
        await browser.close()

    async def demo3(self):
        """
        headless将它设置为 True 或者默认不设置它，在启动的时候我们是看不到任何界面的，如果把它设置为 False，
        那么在启动的时候就可以看到界面了，一般我们在调试的时候会把它设置为 False，在生产环境上就可以设置为 True
        :return:
        """
        browser = await launch(headless=False)
        page = await browser.newPage()
        await page.goto('https://www.baidu.com')
        await asyncio.sleep(100)

    async def demo4(self):
        """
        devtools是否开启开发者模式 调试 . devtools=True，则headless始终为false，会出来界面
        :return:
        """
        browser = await launch(devtools=True)
        page = await browser.newPage()
        await page.goto('https://www.taobao.com')
        await asyncio.sleep(100)

    async def demo5(self):
        """
        --window-size设置分辨率
        禁用"Chrome 正受到自动测试软件的控制" -- args=['--disable-infobars']
        :return:
        """
        width, height = 1600, 900
        browser = await launch(headless=False, args=['--disable-infobars', '--window-size={width},{height}'])
        page = await browser.newPage()
        await page.setViewport({'width': width, 'height': height})
        await page.goto('https://www.taobao.com')
        await asyncio.sleep(100)

    async def demo6(self):
        """
        其实淘宝主要通过 window.navigator.webdriver 来对 webdriver 进行检测，所以我们只需要使用 JavaScript
        将它设置为 false 即可
        :return:
        """
        width, height = 1600, 900
        browser = await launch(headless=False, args=['--disable-infobars', '--window-size={width},{height}'])
        page = await browser.newPage()
        await page.setViewport({'width': width, 'height': height})
        await page.goto('https://www.taobao.com')
        await page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        await asyncio.sleep(100)

    async def demo7(self):
        """
        使用用户目录 在启动的时候设置 userDataDir
        如果设置了它，每次打开就不再是一个全新的浏览器了，它可以恢复之前的历史记录，也可以恢复很多网站的登录信息。
        具体看 https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md
        :return:
        """
        width, height = 1600, 900
        browser = await launch(headless=False, userDataDir='userdata', args=['--disable-infobars', '--window-size={width},{height}'])
        page = await browser.newPage()
        await page.setViewport({'width': width, 'height': height})
        await page.goto('https://www.taobao.com')
        await page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
        await asyncio.sleep(100)


if __name__ == '__main__':
    pd = PyppeteerDemo()
    # asyncio.get_event_loop().run_until_complete(pd.demo1())
    # asyncio.get_event_loop().run_until_complete(pd.demo2())
    asyncio.get_event_loop().run_until_complete(pd.demo7())