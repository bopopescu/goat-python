# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = 'BaiduSpider'
    allowed_domains = ['http://www.baidu.com']
    start_urls = ['http://http://www.baidu.com/']

    def parse(self, response):
        print(response)
        pass
