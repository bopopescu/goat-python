# -*- coding: utf-8 -*-
import scrapy

'''
抓取网页数据 并保存到本地  请求方式二
'''
class App02Spider(scrapy.Spider):
    name = 'app02'

    # 另外一种初始链接写法
    def start_requests(self):
        #爬取的链接由此方法通过下面链接爬取页面
        urls = [ 'http://lab.scrapyd.cn/page/2/', ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('保存文件: %s' % filename)