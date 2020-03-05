# -*- coding: utf-8 -*-
import scrapy

class QsbkspiderSpider(scrapy.Spider):
    # qsbkSpider 爬虫类的类名
    name = 'qsbkSpider'
    # 限制爬虫能够爬取的网址范围
    # allowed_domains = ['qiushibaike.com']
    allowed_domains = ['tianyancha.com']
    #指定从哪个url开始爬取
    start_urls = ['http://tianyancha.com/']

    def parse(self, response):
        print("*"*40)
        print(type(response)) # <class 'scrapy.http.response.html.HtmlResponse'>
        # test = response.xpath("//div[@class='live-search-wrap -index']")
        test = response.xpath("//input[@id='home-main-search']")
        # test = response.xpath("//div[@class='back_to_top']")
        print(test)
        print("*"*40)

        # 解析结果
        results = json.loads(response.text)
        companyList = results.get('data').get('companyList')

        pass


