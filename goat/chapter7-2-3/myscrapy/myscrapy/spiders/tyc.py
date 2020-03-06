# -*- coding: utf-8 -*-
import scrapy


class TycSpider(scrapy.Spider):
    name = 'tyc'
    # allowed_domains = ['tianyancha.com']
    # start_urls = ['http://tianyancha.com/']
    # re = 'https://www.tianyancha.com/search?key='+key_word


    # 另外一种初始链接写法
    def start_requests(self):
        #爬取的链接由此方法通过下面链接爬取页面
        key_word = "山羊公司";
        urls = [ 'https://www.tianyancha.com/search?key='+ key_word ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        myList = response.xpath('//*[@id="web-content"]/div/div[1]/div[2]/div[2]').getAll() #
        name = myList[0].xpath('//*[@id="web-content"]/div/div[1]/div[2]/div[2]/div[1]/div/div[3]/div[1]/a')
        print(name)