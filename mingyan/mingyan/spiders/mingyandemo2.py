# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/22 14:55

import scrapy

"""
提取一组数据
"""

class mingyandemo2(scrapy.Spider):

    name = "mingyandemo2"
    allowed_domains = ["lab.scrapyd.cn"]
    start_urls = [
        'http://lab.scrapyd.cn/page/1/',
    ]


    def parse(self, response):
        mingyans = response.css('div.quote')
        for mingyan in mingyans:
            # class用 . ， id用#，  ::表示任意标签
            text = mingyan.css('.text::text').extract_first()  # 提取名言
            autor = mingyan.css('.author::text').extract_first()  # 提取作者
            tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
            tags = ','.join(tags)  # 数组转换为字符串

            fileName = 'demo2\\%s-语录.txt' % autor  # 爬取的内容存入文件，文件名为：作者-语录.txt
            # fileName = '语录.txt'
            f = open(fileName, "a+", encoding='utf-8')  # 追加写入文件
            f.write(autor)  # 写入作者
            f.write('\n')  # 换行
            f.write(text)  # 写入名言内容
            f.write('\n')  # 换行
            f.write(('标签：' + tags))  # 写入标签
            f.write('\n')  # 换行
            f.close()  # 关闭文件操作、

        next_page = response.css('li.next a::attr(href)').extract_first()   # css选择器提取下一页链接

        if next_page is not None:  # 判断是否存在下一页

            """
             如果是相对路径，如：/page/1
             urljoin能替我们转换为绝对路径，也就是加上我们的域名
             最终next_page为：http://lab.scrapyd.cn/page/2/
            """
            next_page = response.urljoin(next_page)
            """
                      接下来就是爬取下一页或是内容页的秘诀所在：
                      scrapy给我们提供了这么一个方法：scrapy.Request()
                      这个方法还有许多参数，后面我们慢慢说，这里我们只使用了两个参数
                      一个是：我们继续爬取的链接（next_page），这里是下一页链接，当然也可以是内容页
                      另一个是：我们要把链接提交给哪一个函数(callback=self.parse)爬取，这里是parse函数，也就是本函数
                      当然，我们也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
                      经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页

                      """
            yield scrapy.Request(next_page, callback=self.parse)

