# -*- coding: utf-8 -*-
import scrapy


class App08Spider(scrapy.Spider):
    name = 'app08'
    allowed_domains = ['xicidaili.com'] #允许爬取的域名
    # start_urls = ['http://xicidaili.com/']
    start_urls = ['https://www.xicidaili.com/nn/'] #开始采集的网址
    #解析响应数据，提取数据获取网址等  response就是网页源码
    def parse(self, response):
        #1、因为全在tr标签下，拿到tr标签的内容在选择
        trTags = response.xpath('//tr')   #选择所有的tr标签
        for tr in trTags:  #遍历tr标签下的所有的td标签
            ip = tr.xpath('./td[2]/text()').get()  #   ./ 表示在当前节点下继续选择
            port = tr.xpath('./td[3]/text()').get()
            print(ip,port)  #打印ip  port

        '''
        第一页     下一页元素信息   <a class="next_page" rel="next" href="/nn/2">下一页 ›</a>
        最后一页   下一页元素信息   <span class="next_page disabled">下一页 ›</span>
        再由于整个页面中  class属性为next_page的 只有一个 所以可以通过他来判断 是否还有下一页
        有下一页  //a[@class="next_page"]/@href   ===>  /nn/2
        无下一页  //a[@class="next_page"]/@href   ===>  [NULL]
        '''
        #下一页操作
        next_page = response.xpath('//a[@class="next_page"]/@href').get() #  /nn/2
        temp = int(next_page.split("/")[-1])
        if temp>5:
            return
        #拼接网址
        # next_url = "https://www.xicidaili.com"+next_page;
        next_url = response.urljoin(next_page) # https://www.xicidaili.com/nn/2
        #发出请求   Request callback是回调函数，将请求得到响应交给自己处理
        yield scrapy.Request(next_url,callback=self.parse)




