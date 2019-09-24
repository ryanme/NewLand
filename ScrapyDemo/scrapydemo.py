# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/22 14:30

import scrapy

"""
scrapy runspider scrapydemo.py -o mingyan.json
"""


class mingyanSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://lab.scrapyd.cn/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                '内容': quote.css('span.text::text').extract_first(),
                '作者': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, self.parse)
