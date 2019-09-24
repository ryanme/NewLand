# -*- coding: utf-8 -*-
import scrapy


class QishuwangSpider(scrapy.Spider):
    name = 'qishuwang'
    fileName = '神级龙卫.txt'
    allowed_domains = ['https://m.biqutxt.com']
    start_urls = ['https://m.biqutxt.com/84_84627/30428308.html']

    def parse(self, response):
        div = response.css('div#novelbody')
        # class用 . ， id用#，  ::表示任意标签

        # 标题
        title = div.css('div.nr_function.next h1').extract_first()
        # 正文
        content = div.css('div#novelcontent').extract_first()

        f = open(self.fileName, "a+", encoding='utf-8')  # 追加写入文件
        f.write(title)  # 写入作者
        f.write('\n')  # 换行
        f.write(content)  # 写入名言内容
        f.write('\n')  # 换行
        f.close()  # 关闭文件操作、

        next_page = response.css('div.page_chapter1.next ul.next li.p4.next a::attr(href)').extract_first()   # css选择器提取下一页链接

        if next_page is not None:  # 判断是否存在下一页
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

