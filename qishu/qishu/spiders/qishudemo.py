# -*- coding: utf-8 -*-
# @Author  : guowr
# @Time    : 2019/8/27 15:56

import requests
from bs4 import BeautifulSoup
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class QiShuDemo:

    def __init__(self):
        self.session = requests.session()

    def sendReqAndReturnSoup(self, url):
        try:
            tempres = self.session.get(url)
            if not tempres.status_code == 200:
                return False
            response = tempres.content.decode('GBK')
            soup = BeautifulSoup(response, 'lxml')
            return soup
        except Exception as e:
            logger.error(e)
            logger.warning("fail page url=%s" % url)

    def getContent(self, right_url,  pervious_page_name=None):
        url = "https://m.biqutxt.com"+right_url
        res = self.sendReqAndReturnSoup(url)
        if not res:
            return
        page_name = res.select('div[class="page_chapter1"]')[0].previous_sibling.previous_sibling.text  # 章节名
        title = res.select('div[class="nav_name"]')[0].text  # 书名
        content = res.select_one('div[id="novelcontent"]')  # 内容
        next__right_url = res.select_one('div[class="page_chapter"]').select_one('a[class="p4"]').get_attribute_list('href')[0]
        centers = content.select('center')
        for i in centers:
            i.extract()     # 去除无效段落
        fp = open('%s.txt' % title, "a+", encoding='UTF-8')
        if not pervious_page_name == page_name:
            fp.write(page_name)
            fp.write('\n')
        logger.info("success save: %s, right_url is: %s, the next url is:%s" % (page_name, right_url, next__right_url))
        fp.write(content.text.strip())
        if len(centers) == 1:
            fp.write('\n')
        fp.close()
        self.getContent(next__right_url, pervious_page_name=page_name)


if __name__ == '__main__':
    qs = QiShuDemo()
    right_url = "/84_84627/30428903_2.html"
    qs.getContent(right_url)
